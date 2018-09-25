##  @filename: joints.py
#

from servo import Servo
from calibrator import Calibrator
from drivers.PCA9685 import PCA9685

from calibrator import Calibrator

class Joints:
    def __init__(self):
        self.joints = []
        for pin in range(0,12):
            self.joints.append(Servo(pin))
        self._pwm =  PCA9685()
        self._pwm.set_pwm_freq(60)
    def calibrate_all(self):
        calibrator = Calibrator(self.joints)
        calibrator.calibrate()

    def load_joints(self,filename):
        #Find file with calibrated joints
        pass

joints=Joints()
joints.calibrate_all()
