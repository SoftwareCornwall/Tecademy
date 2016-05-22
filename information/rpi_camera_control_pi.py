from picamera import PiCamera
from gpiozero import Button
from time import sleep

button = Button(4, pull_up = False)

camera = PiCamera()
camera.start_preview(alpha=192)

button.wait_for_press()
camera.capture('my_face.jpg')
sleep(3)

