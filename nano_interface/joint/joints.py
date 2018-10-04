##  @filename: joints.py
#

from servo import Servo
from calibrator import Calibrator
from drivers.PCA9685 import PCA9685

class Joints:
    def __init__(self):
        self.joints = []
        self._pwm =  PCA9685()
        for pin in range(0,12):
            self.joints.append(Servo(pin, self._pwm))
            if (pin in set([1,4,7,10])):
                self.joints[pin].set_deg_max(120)
                self.joints[pin].set_deg_min(60)
        self._pwm.set_pwm_freq(60)
    def calibrate_all(self):#add filename
        calibrator = Calibrator(self.joints)
        calibrator.json_calibrate()

    def load_joints(self,filename="calibrator.pickle"):
        #Find file with calibrated joints
        calibrator = Calibrator(self.joints)
        self.joints = calibrator.read_cal(self._pwm,filename)

joints=Joints()
joints.calibrate_all()
#joints.load_joints()
#-------joints.joints[0].actuate(joints._pwm,joints.joints[0]._center)
#joints.joints[0].actuate_deg(90)
