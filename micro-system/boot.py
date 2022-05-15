# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
# import webrepl
# webrepl.start()

from machine import Pin

from manage_network import connect_wireless_network


def clearConsole(): return print('\n' * 25)


clearConsole()

print('= ' * 20 + '\n')

network_error_pin = Pin(15, Pin.OUT)
lcd_error_pin = Pin(0, Pin.OUT)
lcd_error_pin.off()
network_error_pin.off()

sta_if = None

times = 0
while not sta_if:
    print('Started while not sta_if')
    sta_if = connect_wireless_network()
    print('STA_IF: ', sta_if)

    print('Setting sta_if - True')
    sta_if = True
