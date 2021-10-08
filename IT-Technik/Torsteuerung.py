# import RPi.GPIO as GPIO
# import time

# leds = [22, 24, 26, 28]
# sensors = [27, 29, 31, 33]

# # setup pins
# GPIO.setmode(GPIO.BOARD)
# for pin in leds:
#     GPIO.setup(int(pin), GPIO.OUT)
# for pin in sensors:
#     GPIO.setup(int(pin), GPIO.IN)
# # randow infinit loop
# while True:
#     # loop 5 times
#     for i in range(4):
#         # Check sensor
#         state = GPIO.input(sensors[i])
#         # wait a sec    
#         time.sleep(1)
#         # set state of LED
#         GPIO.output(leds[i], state)