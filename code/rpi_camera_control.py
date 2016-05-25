from microbit import *

while True:

    if button_a.is_pressed():
        display.scroll("Say cheese!")
        
        pin1.write_digital(1)
        sleep(2000)
 
    pin1.write_digital(0)