##  @filename: joints.py
#

from servo import Servo
from calibrator import Calibrator
from drivers.PCA9685 import PCA9685

class Joints:
    def __init__(self):
        self.joints = []
        for pin in range(0,12):
            self.joints.append(Servo(pin))
        self._pwm =  PCA9685()
        self._pwm.set_pwm_freq(60)
    def calibrate_all(self):#add filename
        calibrator = Calibrator(self.joints)
        calibrator.calibrate(self._pwm)

    def load_joints(self,filename="calibrator.pickle"):
        #Find file with calibrated joints
        calibrator = Calibrator(self.joints)
        self.joints = calibrator.read_cal()

joints=Joints()
#joints.calibrate_all()
joints.load_joints()
#joints.joints[0].actuate(joints._pwm,joints.joints[0]._deg90)
joints.joints[0].off(joints._pwm)
