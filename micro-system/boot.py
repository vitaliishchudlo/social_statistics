import time
import network
import json
from statuses import *
from machine import Pin
from machine import SoftI2C, Pin
from mp_i2c_lcd1602 import LCD1602
from manage_network import connect_wireless_networks

print('\n' * 25 + '= ' * 10 + 'ESP-32 Started ' + '= ' * 10 + '\n')


# Error pins initialization

network_error_pin = Pin(15, Pin.OUT)
network_error_pin.on()
lcd_error_pin = Pin(0, Pin.OUT)
lcd_error_pin.on()

# Remove in future!!!!!
network_error_pin.off()
# lcd_error_pin.off()


# Starting booting the system

# = = = = = = = LCD = = = = = = = = =
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)

try:
    addr = i2c.scan()
    if not len(addr) == 1:
        lcd_error_pin.on()
        lcd_status = False
    else:
        lcd_error_pin.off()
        lcd_status = True
except Exception:
    pass

lcd = LCD1602(i2c)


# = = = = = = = Network = = = = = = = = =

sta_if = network.WLAN(network.STA_IF)
if not sta_if.active():
    sta_if.active(True)

if not connect_wireless_network():
    print('No success')
else:
    print('success')


# while not sta_if.is

# while not sta_if_status:
#    print('Started while not sta_if')
#    sta_if = connect_wireless_network()
#    print('STA_IF: ', sta_if_status)
#    print('Setting sta_if - True')
#    sta_if_status = True
