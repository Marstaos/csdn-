# 这是考核时间内的第一份存档。
# 在这份代码中实现了光敏原件对环境光的实时感知，并可以回传状态到手机app.
from Blinker.Blinker import Blinker, BlinkerNumber
from Blinker.BlinkerDebug import *
import RPi.GPIO as GPIO
auth = '260a35733aa0'  # 这是我的设备密钥
BLINKER_DEBUG.debugAll()
Blinker.mode('BLINKER_WIFI')
Blinker.begin(auth)

import time
from time import sleep
GPIO.setmode(GPIO.BOARD)  
GPIO.setwarnings(False)
pin_pqrs=18  #设置光敏传感器的引脚
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_pqrs, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


d=BlinkerNumber('d1')  #d1是手机app上一个文字区块的名字。这行代码使得回传数据能够正确定位到手机app上的那个显示区块。

if __name__ == '__main__':
    while 1:  #设置循环，开始感知环境光照并回传数据
        Blinker.run()
        status = GPIO.input(pin_pqrs)
        if status == False:
            a = "light is ok!"  #此处使用a来记录回传的字符串
        else:
            a = "too dark!"
        Blinker.delay(1000)
        d.print(a)  #此处将a中记录的信息回传给手机。
        time.sleep(2)  #设置两秒的延迟
