from microbit import *
import random

random.seed(1337)

while True:
    display.show(Image.ALL_CLOCKS, loop=False, delay=100)

    if button_a.is_pressed() and button_b.is_pressed():
        rand = random.randint(1,100)

        if(rand > 30):
            image = Image.HEART
        else:
            image = Image.SAD

        while button_a.is_pressed() and button_b.is_pressed():
            display.show(image)