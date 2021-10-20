import RPi.GPIO as GPIO
from time import sleep, time
from KeyDictionnary import keys_dict, test_string

left_1 = 5
left_2 = 6
left_3 = 13
left_4 = 19
left_5 = 26
left_6 = 16
left_7 = 20
left_8 = 21

right_1 = 4
right_2 = 17 
right_3 = 18 
right_4 = 27 
right_5 = 22 
right_6 = 24 
right_7 = 23 
right_8 = 25 

class AutoTypewriter():
    def __init__(self):

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(left_1, GPIO.IN)
        GPIO.setup(left_2, GPIO.IN)
        GPIO.setup(left_3, GPIO.IN)
        GPIO.setup(left_4, GPIO.IN)
        GPIO.setup(left_5, GPIO.IN)
        GPIO.setup(left_6, GPIO.IN)
        GPIO.setup(left_7, GPIO.IN)
        GPIO.setup(left_8, GPIO.IN)


        GPIO.setup(right_1, GPIO.OUT, initial=1)
        GPIO.setup(right_2, GPIO.OUT, initial=1)
        GPIO.setup(right_3, GPIO.OUT, initial=1)
        GPIO.setup(right_4, GPIO.OUT, initial=1)
        GPIO.setup(right_5, GPIO.OUT, initial=1)
        GPIO.setup(right_6, GPIO.OUT, initial=1)
        GPIO.setup(right_7, GPIO.OUT, initial=1)
        GPIO.setup(right_8, GPIO.OUT, initial=1)

    def press_key(self, keys):
        emit, receive, shift_pressed = keys
        if shift_pressed:
            emit_shift, receive_shift, shift_pressed = keys_dict["shift"]        
            before = time()
            while(time()-before < 0.05):
                GPIO.output(receive_shift, GPIO.input(emit_shift))            
            before = time()
            while(time()-before < 0.1):
                GPIO.output(receive_shift, GPIO.input(emit_shift))
                GPIO.output(receive, GPIO.input(emit))
            GPIO.output(receive_shift, 1)
            GPIO.output(receive, 1)
        else:
            before = time()
            while(time()-before < 0.1):
                GPIO.output(receive, GPIO.input(emit))
            GPIO.output(receive, 1)
        sleep(0.1)

    def press_string(self, string):
        for char in string:
            self.press_key(keys_dict[char])
        

