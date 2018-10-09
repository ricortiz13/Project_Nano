##  @file: servo.py
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
        self._polarity_on = False

    def actuate(self, pwm_pos):
        self._curr_pwm = pwm_pos
        self._pwm_board.set_pwm(self._pin,0,self._curr_pwm)
    def actuate_deg(self, deg_pos):
        #TODO convert repeated code into functions
        # Convert to pwm
        if (self._polarity_on):
            deg_pos = 180 - deg_pos
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
        self._curr_deg = deg_pos
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

    def get_pos(self):
        return self._curr_deg
    def get_pwm(self):
        return self._curr_pwm
    def change_polarity(self,polarity_on=True):
        if (polarity_on and not(self._polarity_on)):
            #polarized
            self._polarity_on = True
            #polar_switch = self._pwm_min
            #self._pwm_min = self._pwm_max
            #self._pwm_max = polar_switch

            #polar_switch = self._deg_min
            #self._deg_min = self._deg_max
            #self._deg_max = polar_switch

        elif (not(polarity_on) and self._polarity_on):
            #normal way
            self._polarity_on = False
            #polar_switch = self._pwm_min
            #self._pwm_min = self._pwm_max
            #self._pwm_max = polar_switch

            #polar_switch = self._deg_min
            #self._deg_min = self._deg_max
            #self._deg_max = polar_switch

if __name__ == "__main__":
    #turn all off
    from drivers.PCA9685 import PCA9685
    pwm = PCA9685()
    for i in range(0,12):
        Servo(i,pwm).off()
