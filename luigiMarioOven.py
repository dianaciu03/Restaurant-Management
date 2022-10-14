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
timerTime = 60



board.displayOff()


while(True):


    #read button state
    buttonstate = board.digital_read(BUTTON1PIN)
    buttonstate1 = board.digital_read(BUTTON2PIN)
    time.sleep(0.3)
  
    
    
    #if button pressed adjust variable
    if buttonstate[0] == 0:
        buttonToggled = True
    
    if buttonstate1[0] == 0:
        buttonToggled1 = True
        
    if ready == True:
        readyinside = True
        while readyinside == True:
            board.pwm_write(TONE_PIN, 250)
            time.sleep(0.3)
            board.set_pin_mode_pwm_output(TONE_PIN)
            time.sleep(0.3)
            buttonstate1 = board.digital_read(BUTTON2PIN)
            if buttonstate1[0] == 0:
                readyinside = False
                
    if buttonToggled1 == True:
        if ready == True:
            board.digital_write(GREENLIGHTPIN, 0)
            buttonToggled1 = False
            ready = False
            board.displayOff()

    
    #if button pressed
    if buttonToggled == True and ready == False:
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
        #reset timer
        timerTime = 60
        board.digital_write(REDLEDPIN, 0)
        time.sleep(0.3)
        board.digital_write(GREENLIGHTPIN, 1)
        ready = True
        
    #reset button toggle
    buttonToggled = False
    buttonToggled1 = False
 
