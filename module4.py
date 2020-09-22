import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
pwn = GPIO.PWM(12, 50)
pwn.start(0)
try:
    while True:
        for i in range(100):
            pwn.ChangeDutyCycle(i)
            time.sleep(0.1)
        for i in range(100, 0, -1):
            pwn.ChangeDutyCycle(i)
            time.sleep(0.1)
except KeyboardInterrupt:
    pwn.stop()
    GPIO.cleanup()
