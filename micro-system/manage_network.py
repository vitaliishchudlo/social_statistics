import json
import time

import network


def connect_wireless_network():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.active():
        sta_if.active(True)

    with open('config.json', 'r') as file:
        result = json.loads(file.read())
        ssid = result['network']['ssid']
        password = result['network']['password']

    if ssid and password:
        print('There is some data')
        sta_if.connect(ssid, password)
        for x in range(16):
            if not sta_if.isconnected():
                print('Trying to connect to "%s" | %s/15' % (ssid, x))
                time.sleep(1)
            else:
                print('Connected')
                break
        if sta_if.isconnected():
            return sta_if
    return False
