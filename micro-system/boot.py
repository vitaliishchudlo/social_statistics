import sys

import machine
import network
import ubinascii
from libraries.lib_lcd1602_2004_with_i2c import LCD
from machine import SoftI2C, Pin
from microdot_asyncio import Microdot, Response

from html_handler import *
from statuses import *

print('\n' * 25 + '= ' * 10 + 'ESP-32 Started ' + '= ' * 10 + '\n')

# Error pins initialization

network_error_pin = Pin(15, Pin.OUT)
network_error_pin.off()
lcd_error_pin = Pin(0, Pin.OUT)
lcd_error_pin.off()

# Starting booting the system

# = = = = = = = LCD = = = = = = = = =
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)

try:
    addr = i2c.scan()
    if not len(addr) == 1:
        lcd_error_pin.on()
        lcd_status = False
        sys.exit()
    else:
        lcd_error_pin.off()
        lcd_status = True
except Exception:
    lcd_error_pin.on()
    lcd_status = False
    sys.exit()

# lcd = LCD1602(i2c)
lcd = LCD(SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000))

# = = = = = = = Network = = = = = = = = =

wlan = network.WLAN(network.STA_IF)
if not wlan.active():
    wlan.active(True)


def wlan_connected():
    if wlan.isconnected():
        wlan_status = True
        for x in range(5):
            lcd.backlight(True)
            network_error_pin.on()
            time.sleep(0.7)
            lcd.backlight(False)
            network_error_pin.off()
            time.sleep(0.7)
        lcd.clear()
        lcd.backlight(True)
        return


def wlan_connect(lcd, ssid=None, password=None):
    lcd.clear()
    if wlan_status:
        return True
    if not ssid or not password:
        config_json = read_config_file()
        ssid = config_json['network']['ssid']
        password = config_json['network']['password']
    if ssid and password:
        wlan.connect(ssid, password)
        for x in range(11):
            if not wlan.isconnected():
                lcd.puts(ssid, 0, 0)
                lcd.puts('      ' + str(x) + '/10', 0, 1)
                time.sleep(0.5)
            else:
                lcd.clear()
                lcd.puts(ssid, 0, 0)
                lcd.puts('   Connected', 0, 1)
                wlan_connected()
                break
        if wlan.isconnected():
            write_network(ssid, password)
            return True
    delete_network()
    return False


if wlan_connect(lcd):
    wlan_status = True
    wlan_ip = wlan.ifconfig()[0]
    sys.exit()

network_error_pin.on()
wlan_status = False
lcd.clear()
lcd.puts('WLAN ERROR', 4, 0)
time.sleep(3)

ap = network.WLAN(network.AP_IF)
ap_ssid = 'ESP-WiFiManager'
ap_password = ubinascii.hexlify(machine.unique_id()).decode("utf-8")[:10]
ap.active(True)
ap.config(essid=ap_ssid, password=ap_password, authmode=4)

lcd.clear()

lcd.puts('WeFi SetUp', 5, 0)
lcd.puts('Name:' + ap_ssid, 0, 1)
lcd.puts('Pass:' + ap_password, 0, 2)
lcd.puts('IP: ' + ap.ifconfig()[0], 0, 3)

# Добавити штуку в паралельному потоці, де б писалася вся потрібна..
# .. інфа та були в ній стопери (self.pause, self.break)

ap_wifimanager = Microdot()


@ap_wifimanager.route('/', methods=["GET", "POST"])
async def choose_network(request):
    ap.disconnect()
    available_networks = [x[0].decode('utf-8') for x in ap.scan()]
    response_html = response_choose_network(available_networks)
    return Response(body=response_html, headers={"Content-Type": "text/html"})


@ap_wifimanager.post('/configure')
async def configure_network(request):
    try:
        request.form['ssid']
    except KeyError:
        return Response(body=bad_wifi_credentials('None', 'You didn`t choose the WiFi'),
                        headers={"Content-Type": "text/html"})
    ssid = request.form['ssid']
    if not request.form['password']:
        return Response(body=bad_wifi_credentials(ssid, 'You didn`t enter the password'),
                        headers={"Content-Type": "text/html"})
    password = request.form['password']
    if len(password) < 8:
        return Response(body=bad_wifi_credentials(ssid, 'Password must be 8 characters or more'),
                        headers={"Content-Type": "text/html"})
    if not wlan_connect(lcd, ssid=ssid, password=password):
        response_html = bad_wifi_credentials(ssid, 'You entered bad password')
        return Response(body=response_html, headers={"Content-Type": "text/html"})
    wlan_status = True
    ap_wifimanager.shutdown()
    return Response(body='Successfully! The server is shutting down...', headers={"Content-Type": "text/plain"})


ap_wifimanager.run(host=ap.ifconfig()[0], port=80)

wlan_connected()
wlan_ip = wlan.ifconfig()[0]

ap.active(False)
