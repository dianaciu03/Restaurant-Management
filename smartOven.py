from operator import truediv
import time, sys
from fhict_cb_01.CustomPymata4 import CustomPymata4

#-----------
# Constants
#-----------
BUTTON1PIN = 8
BUTTON2PIN = 9
REDLEDPIN = 4
GREENLIGHTPIN = 5
TONE_PIN = 3


board = CustomPymata4(com_port= "COM3")
board.set_pin_mode_digital_input_pullup(BUTTON1PIN) #button
board.set_pin_mode_digital_input_pullup(BUTTON2PIN) #button
board.set_pin_mode_pwm_output(TONE_PIN)

time.sleep(0.3)
buttonToggled = False
buttonToggled1 = False
ready = False
timerTime = 5
    
    
    
  
#set timer
board.displayOn()
while timerTime != -1:
    time.sleep(1)
    print(timerTime)
    ty_res = time.gmtime(timerTime)
    timeshow = time.strftime("%M%S",ty_res)
    print(timeshow)
    board.displayShow(timeshow)
    timerTime -= 1
    board.digital_write(REDLEDPIN, 1)

board.digital_write(REDLEDPIN, 0)
time.sleep(0.3)
board.digital_write(GREENLIGHTPIN, 1)   
    
readyinside = True
while readyinside == True:
    board.pwm_write(TONE_PIN, 250)
    time.sleep(0.3)
    board.set_pin_mode_pwm_output(TONE_PIN)
    time.sleep(0.3)
    buttonstate1 = board.digital_read(BUTTON2PIN)
    if buttonstate1[0] == 0:
        readyinside = False
        board.digital_write(GREENLIGHTPIN, 0)
        board.displayOff()
        
board.shutdown()
