##  @file: calibrator.py
#   @author: Ricardo Ortiz
#

import pickle
from servo import Servo
from iterator import List_Iterator

class Calibrator:
    def __init__(self,servos):
        self._servos = servos
        self.iterator = List_Iterator(self._servos)
    def calibrate (self, pwm_gen):
        joint = "0"
        angle = ["0","90","180"]
        pwm = 250
        i = 0
        while(not(self.iterator.isDone())):
            print("Joint "+ joint + ", angle "+ angle[i]+" | PWM: " + str(pwm))
            usr = input("Enter q[+], a[-], or z[submit]")
            if (usr == "q"):
                pwm+=5
                self.iterator.get_current().actuate(pwm_gen, pwm)
            elif (usr == "a"):
                pwm-=5
                self.iterator.get_current().actuate(pwm_gen, pwm)
            elif (usr == "z"):
                #accept
                if(i==0):
                    self.iterator.get_current().set_deg0(pwm)
                elif(i==1):
                    self.iterator.get_current().set_deg90(pwm)
                elif(i==2):
                    self.iterator.get_current().set_deg180(pwm)
                    joint = str(int(joint)+1)
                    self.iterator.next()
                i+=1
                i%=3
                pwm=250
            else:
                print("Invalid entry")
        self.write_cal()
    def write_cal(self, filename="calibrator.pickle"):
        data_to_pickle = self.iterator.get_list()
        pickle_file = open(filename,"wb")#wb = write bytes
        pickle.dump(data_to_pickle, pickle_file)
        pickle_file.close()
    def read_cal(self, filename="calibrator.pickle"):
        pickle_file = open(filename,"rb")
        recovered_list = pickle.load(pickle_file)
        pickle_file.close()
        return recovered_list
