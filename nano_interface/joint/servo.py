##  @filename: servo.py
#

class Servo:
    def __init__(self,pin,pwm_generator):
        self._pin = pin
        self._pwm_board = pwm_generator

        self._curr_pwm = 250
        self._pwm_min = 250
        self._pwm_center = 250
        self._pwm_max = 250

        self._curr_deg = 90
        self._deg_min = 0
        self._deg_center = 90
        self._deg_max = 180

    def actuate(self, pwm_pos):
        self._curr_pwm = pwm_pos
        self._pwm_board.set_pwm(self._pin,0,self._curr_pwm)
    def actuate_deg(self, deg_pos):
        # Convert to pwm
        if (deg_pos == 90):
            self._curr_pwm = self._pwm_center
        elif (deg_pos < 90):
            #interpolate between min and center
            self._curr_pwm = ((self._pwm_center - self._pwm_min)/(self._deg_center - self._deg_min))
            self._curr_pwm = self._curr_pwm * (deg_pos - self._deg_min)
            self._curr_pwm = self._curr_pwm + self._pwm_min
            self._curr_pwm = int(self._curr_pwm)
        else:
            #interpolate between center and max
            self._curr_pwm = ((self._pwm_max - self._pwm_center)/(self._deg_max - self._deg_center))
            self._curr_pwm = self._curr_pwm * (deg_pos - self._deg_center)
            self._curr_pwm = self._curr_pwm + self._pwm_center
            self._curr_pwm = int(self._curr_pwm)

        self._pwm_board.set_pwm(self._pin,0,self._curr_pwm)
    def on(self):
        self._pwm_board.set_pwm(self._pin,0,self._curr_pwm)
    def off(self):
        self._pwm_board.set_pwm(self._pin,0,0)
        
    def set_pwm_min(self, pwm):
        self._pwm_min = pwm
    def set_pwm_center(self, pwm):
        self._pwm_center = pwm
    def set_pwm_max(self, pwm):
        self._pwm_max = pwm
    def set_deg_min(self, deg):
        self._deg_min = deg
    def set_deg_max(self, deg):
        self._deg_max = deg

    ##@TODO: This method is obsolete. Delete once all dependencies are removed
    def reference(self, ref=None):
        self._pwm_board = ref
