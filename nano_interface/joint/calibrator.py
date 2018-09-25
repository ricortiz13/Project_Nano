##  @file: calibrator.py
#   @author: Ricardo Ortiz
#

import pickle
from servo import Servo
from list_iterator import List_Iterator

class Calibrator:
    def __init__(self,servos):
        self._servos = servos
        self.iterator = List_Iterator(self._servos)
    def calibrate (self):
        joint = "0"
        angle = ["0","90","180"]
        pwm = 250
        i = 0
        while(not(iterator.isDone())):
            print("Joint "+ joint + ", angle "+ angle[i])
            usr = input("Enter q[+], a[-], or z[submit]")
            if (usr == "q"):
                pwm+=5
            elif (usr == "a"):
                pwm-=5
            elif (usr == "z"):
                #accept
                if(i==0):
                    iterator.get_current().set_deg0(pwm)
                elif(i==1):
                    iterator.get_current().set_deg90(pwm)
                elif(i==2):
                    iterator.get_current().set_deg180(pwm)
                i+=1
                i%=2
                pwm=250
            else:
                print("Invalid entry")
    def write_cal(self, filename):
        pass
    def read_cal(self, filename):
        pass
