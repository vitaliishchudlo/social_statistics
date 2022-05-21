import time

# Remove in future
print('WAITING 1 SECOND BEFORE START!!!!')
time.sleep(1)

# --------------------------------------------

abc = 0

while abc < 16:
    try:
        lcd.puts('Timers: ' + str(abc))
        lcd_error_pin.off()
        lcd_status = True
    except OSError:
        dlcd_error_pin.on()
        lcd_status = False
        print('LCD Broken')
    finally:
        print('sleeping ' + str(abc))
        time.sleep(1)
    abc += 1

print('finish')
