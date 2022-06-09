import json
import network
import time

from boot import lcd


def connect_wireless_network():
    with open('config.json', 'r') as file:
        result = json.loads(file.read())
        ssid = result['network']['ssid']
        password = result['network']['password']

    if ssid and password:
        print('There is some data')
        sta_if.connect(ssid, password)
        print('okay')
        for x in range(16):
            if not sta_if.isconnected():
                print('trying')
                # lcd.puts('Trying to connect to ' 0, 0)
                #lcd.puts(ssid + ' ' + x + '/15', 0, 1)
                time.sleep(0.7)
            else:
                # lcd.puts('Connected')
                print('connected')
                break
        if sta_if.isconnected():
            return True
    return False
