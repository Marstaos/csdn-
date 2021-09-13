#!/usr/bin/python
# encoding:utf-8
import RPi.GPIO as GPIO
import time
from time import sleep

led = 37
flg = False
pin_pqrs=18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_pqrs, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led, GPIO.OUT)
try:
    while True:
        status = GPIO.input(pin_pqrs)
        if status == False:
            print('Light is ok')
            flg = False
            GPIO.output(led, flg)
            time.sleep(2)
        else:
            print('Too dark')
            flg = True
            GPIO.output(led, flg)
            time.sleep(2)
except KeyboradInterrupt:
    print("用户停止")
    GPIO.cleanup()
