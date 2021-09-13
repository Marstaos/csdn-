# 这是第三份存档，可以实现手机点按钮控制灯的开闭
from Blinker import Blinker,BlinkerButton
from Blinker.BlinkerDebug import *
import RPi.GPIO as GPIO
auth = "260a35733aa0"  
BLINKER_DEBUG.debugAll()
Blinker.mode("BLINKER_WIFI")   
Blinker.begin(auth)
button = BlinkerButton("btn-light")   
GPIO.setmode(GPIO.BOARD)  
GPIO.setwarnings(False)
GPIO.setup(37,GPIO.OUT,initial=GPIO.LOW)
light1 = 0  
def button_callback(state):
    global light1
    BLINKER_LOG('Button state:',state)
    #light1 = GPIO.output(37, not GPIO.input(37) )
    if light1 == 1:
        GPIO.output(37,0)
        light1 = 0
    else:
        GPIO.output(37,1)
        light1 = 1
    button.print(state)
def data_callback(data):
    BLINKER_LOG("Blinker readString: ",data);
button.attach(button_callback)
if __name__ == '__main__':
    while True:
        Blinker.run()
