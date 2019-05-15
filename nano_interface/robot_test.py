from builder import Robot_Builder
import time

if __name__ == "__main__":
    builder = Robot_Builder()
    builder.build()
    robot = builder.get_build()
    
    height = 60 #[cm]

    while True:
        t = 0.1

        if height>130:
            height=130

        print("height value: " + str(height))

        # Extend all legs of the robot to the specified height
        # This loop will make the robot rise with all four legs incrementing 
        # with a vertical end-effector path
        robot.controller(height, 'fr')
        robot.controller(height, 'fl')
        robot.controller(height, 'br')
        robot.controller(height, 'bl')
        time.sleep(t)
        height+=5
