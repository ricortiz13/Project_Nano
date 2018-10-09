from builder import Robot_Builder
import time

if __name__ == "__main__":
    builder = Robot_Builder()
    builder.build()
    robot = builder.get_build()
    
    while True:
        t = 4
        ##R w R
        ##L w L

        #reach
        robot.reach('fr')
        robot.push('br')
        robot.push('fl')
        robot.push('bl')
        
        time.sleep(t)

        #compress
        robot.compress('fr')
        robot.reach('fl')

        robot.compress('bl')
        
        time.sleep(t)

        #push
        robot.push('fr')
        robot.compress('fl')

        robot.reach('bl')
        robot.compress('br')
        time.sleep(t)

        #retract
        robot.retract('fr')
        robot.push('fl')

        robot.retract('bl')
        robot.reach('br')
        time.sleep(t)

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