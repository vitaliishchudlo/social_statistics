import time


print('MAIN.PY')
if not wlan_status:
    print('exiting main')
    sys.exit()
lcd.clear()
lcd.puts('HELLO MAIN.pY')
sys.exit()

# Remove in future
print('\n\n WAITING 1 SECOND BEFORE START!!!!')
time.sleep(1)

# --------------------------------------------

abc = 0
lcd.clear()

while abc < 16:
    try:
        lcd.puts('Timers: ' + str(abc))
        lcd_error_pin.off()
        lcd_status = True
    except OSError as err:
        # LCD - 116 | Network - -202
        if err.value == 116:
            lcd_error_pin.on()
            lcd_status = False
            print('LCD Broken')
        if err.value == -202:
            network_error_pin.on()
            wlan_status = False
            print('Network broken')
    finally:
        print('sleeping ' + str(abc))
        #time.sleep(1)
    abc += 1

print('FINISHING')

