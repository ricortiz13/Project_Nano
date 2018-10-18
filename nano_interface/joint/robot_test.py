from builder import Robot_Builder
import time

if __name__ == "__main__":
    builder = Robot_Builder()
    builder.build()
    robot = builder.get_build()
    
    y = 60

    while True:
        t = 0.1

        

        if y>130:
            y=130

        # robot.controller(120,'fl')
        # time.sleep(t)

        # robot.controller(70, 'fl')
        # time.sleep(t)
        print("Y value: " + str(y))
        robot.controller(y, 'fr')
        robot.controller(y, 'fl')
        robot.controller(y, 'br')
        robot.controller(y, 'bl')
        time.sleep(t)
        y+=5




        ##R w R
        ##L w L

        #reach

        # #---------------------
        # robot.reach('fr')
        # robot.push('br')
        # robot.push('fl')
        # robot.push('bl')
        
        # time.sleep(t)

        # #compress
        # robot.compress('fr')
        # robot.reach('fl')

        # robot.compress('bl')
        
        # time.sleep(t)

        # #push
        # robot.push('fr')
        # robot.compress('fl')

        # robot.reach('bl')
        # robot.compress('br')
        # time.sleep(t)

        # #retract
        # robot.retract('fr')
        # robot.push('fl')

        # robot.retract('bl')
        # robot.reach('br')
        # time.sleep(t)

        #-----------------

        #----------------------------------------
        #robot.extend('fr')
        #robot.extend('fl')
        #robot.fold('br')
        #robot.fold('bl')

        #time.sleep(1)
    
        #robot.extend('br')
        #robot.extend('bl')
        #robot.fold('fr')
        #robot.fold('fl')

        #time.sleep(1)