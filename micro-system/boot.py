# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
# mport webrepl
# webrepl.start()

from manage_network import connect_wireless_network
print('\n\n')


sta_if = None

times = 0
while not sta_if:
    print('Started while not sta_if')
    sta_if = connect_wireless_network()
    print('STA_IF: ', sta_if)

    print('Setting sta_if - True')
    sta_if = True
