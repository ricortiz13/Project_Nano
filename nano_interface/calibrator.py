##  @file: calibrator.py
#   @author: Ricardo Ortiz
#

import pickle
from .servo import Servo
from .iterator import List_Iterator
from .json_manager import JSON_Manager

class Calibrator:
    def __init__(self,servos):
        self.iterator = List_Iterator(servos)
        self._json_data = dict()
    def calibrate (self):
        joint = "0"
        angle = ["min","center","max"]
        pwm = 250
        i = 0
        while(not(self.iterator.isDone())):
            print("Joint "+ joint + ", set angle to "+ angle[i]+" | PWM: " + str(pwm))
            self.iterator.get_current().actuate(pwm)
            usr = input("Enter q[+], a[-], or z[submit]")
            if (usr == "q"):
                pwm+=5
                self.iterator.get_current().actuate(pwm)
            elif (usr == "a"):
                pwm-=5
                self.iterator.get_current().actuate(pwm)
            elif (usr == "z"):
                #accept
                if(i==0):
                    self.iterator.get_current().set_pwm_min(pwm)
                elif(i==1):
                    self.iterator.get_current().set_pwm_center(pwm)
                elif(i==2):
                    self.iterator.get_current().set_pwm_max(pwm)
                    joint = str(int(joint)+1)
                    self.iterator.next()
                i+=1
                i%=3
                pwm=250
            else:
                print("Invalid entry")
        self.write_cal()
    def json_calibrate (self):
        joint = "0"
        angle = ["min","center","max"]
        pwm = 250
        i = 0
        sub_dict = dict()
        while(not(self.iterator.isDone())):
            print("Joint "+ joint + ", set angle to "+ angle[i]+" | PWM: " + str(pwm))
            self.iterator.get_current().actuate(pwm)
            usr = input("Enter q[+], a[-], or z[submit]")
            if (usr == "q"):
                pwm+=5
                self.iterator.get_current().actuate(pwm)
            elif (usr == "a"):
                pwm-=5
                self.iterator.get_current().actuate(pwm)
            elif (usr == "z"):
                #accept
                if(i==0):
                    #self.iterator.get_current().set_pwm_min(pwm)
                    #self._json_data[int(i)] = dict()
                    #self._json_data[int(i)]["pwm_min"] = pwm
                    #self._json_data[int(i)].update({"pwm_min":pwm})
                    sub_dict["pwm_min"] = pwm
                elif(i==1):
                    #self.iterator.get_current().set_pwm_center(pwm)
                    #self._json_data[int(i)]["pwm_center"] = pwm
                    #self._json_data[int(i)].update({"pwm_center":pwm})
                    sub_dict["pwm_center"] = pwm
                elif(i==2):
                    #self.iterator.get_current().set_pwm_max(pwm)
                    #self._json_data[int(i)]["pwm_max"] = pwm
                    sub_dict["pwm_max"] = pwm
                    #self._json_data[int(i)].update({"pwm_max":pwm})
                    #self._json_data[int(i)] = sub_dict
                    self._json_data.update({int(joint):sub_dict})
                    sub_dict = dict()
                    joint = str(int(joint)+1)
                    self.iterator.next()
                i+=1
                i%=3
                pwm=250
            else:
                print("Invalid entry")
        #self.write_cal()
        print(self._json_data)
        JSON_Manager().write(self._json_data)
    def write_cal(self, filename="calibrator.pickle"):
        self.iterator.first()
        while(not(self.iterator.isDone())):
            self.iterator.get_current().reference()
            self.iterator.next()
        data_to_pickle = self.iterator.get_list()
        pickle_file = open(filename,"wb")#wb = write bytes
        pickle.dump(data_to_pickle, pickle_file)
        pickle_file.close()
    def read_cal(self, pwm_board, filename="calibrator.pickle"):
        pickle_file = open(filename,"rb")
        recovered_list = pickle.load(pickle_file)
        pickle_file.close()
        iterator = List_Iterator(recovered_list)
        while(not(iterator.isDone())):
            iterator.get_current().reference(pwm_board)
            iterator.next()
        return iterator.get_list()
