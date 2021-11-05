import RPi.GPIO as GPIO
from time import sleep, time
from KeyDictionnary import keys_dict, test_string
import threading

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

PRESS_TIME = 0.05

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

        self.cancel_action = False
        self.running = False
        self.t = None

    def press_key(self, keys):
        emit, receive, shift_pressed, code_pressed = keys
        if shift_pressed:
            emit_shift, receive_shift, shift_pressed_shift, code_pressed_shift = keys_dict["shift"]
            emit_shift_lck, receive_shift_lck, shift_pressed_shift_lck, code_pressed_shift_lck = keys_dict["shiftlock"]
            before = time()
            while(time()-before < PRESS_TIME):
                GPIO.output(receive_shift_lck, GPIO.input(emit_shift_lck))
            GPIO.output(receive_shift_lck, 1)
            before = time()
            while(time()-before < PRESS_TIME):
                GPIO.output(receive, GPIO.input(emit))
            GPIO.output(receive, 1)
            before = time()
            while(time()-before < PRESS_TIME):
                GPIO.output(receive_shift, GPIO.input(emit_shift))
            GPIO.output(receive_shift, 1)
            sleep(PRESS_TIME*1)
        elif code_pressed:
            emit_code, receive_code, shift_pressed_code, code_pressed_code = keys_dict["unknown_6"]
            before = time()
            while(time()-before < PRESS_TIME):
                GPIO.output(receive_code, GPIO.input(emit_code))
            before = time()
            while(time()-before < PRESS_TIME):
                GPIO.output(receive, GPIO.input(emit))
            GPIO.output(receive_code, 1)
            GPIO.output(receive, 1)
            sleep(PRESS_TIME)
        else:
            before = time()
            while(time()-before < PRESS_TIME):
                GPIO.output(receive, GPIO.input(emit))
            GPIO.output(receive, 1)
        sleep(0.1)

    def underline_press_key(self, keys):
        self.press_key(keys)
        self.press_key(keys_dict["return"])
        self.press_key(keys_dict["return"])
        self.press_key(keys_dict["_"])

    def press_string(self, string):
        self.running = True
        for char in string:
            if self.cancel_action:
                self.cancel_action = False
                print("Break press_string")
                break
            self.press_key(keys_dict[char])
        self.running = False

    # use  '@@' to delimit
    def underline_delimiter_press_string(self, string):
        last_char = ""
        underline_enabled = False
        self.running = True

        str_index  = 0
        while str_index < len(string):            
            if self.cancel_action:
                self.cancel_action = False
                print("Break underline_delimiter_press_string")
                break
            if string[str_index] == "@" and str_index+1 < len(string) and string[str_index+1] == "@":
                underline_enabled = not(underline_enabled)
                str_index+=1
            else:
                if underline_enabled:
                    self.underline_press_key(keys_dict[string[str_index]])
                else:
                    self.press_key(keys_dict[string[str_index]])
            str_index +=1
        
        self.running = False

    def underline_press_string(self, string):
        self.running = True
        for char in string:
            if self.cancel_action:
                self.cancel_action = False
                print("Break underline_press_string")
                break
            self.underline_press_key(keys_dict[char])
        self.running = False

    def wait_cancel_thread(self):
        if self.t != None:
            self.cancel_action = True
            while(self.t.is_alive()):
                sleep(0.1)

    def threaded_press_string(self, string):
        self.wait_cancel_thread()
        self.cancel_action = False
        self.t = threading.Thread(target=self.press_string, args=(string,))
        self.t.start()

    def threaded_underline_delimiter_press_string(self, string):
        self.wait_cancel_thread()
        self.cancel_action = False
        self.t = threading.Thread(target=self.underline_delimiter_press_string, args=(string,))
        self.t.start()

    def cancel(self):
        if self.t != None and self.t.is_alive():
            self.cancel_action = True
            print("Cancel action")



