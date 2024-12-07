from hub import light_matrix, motion_sensor, port
import runloop
import motor_pair
from app import display
import motor

# declare constants
ROTATION_TO_CM = 28 #17.2787595947
#right attachment is port D and Left attachment is port E
WHEELRIGHTPORT= port.F
WHEELLEFTPORT = port.B
FRONTATTACMENTPORT = port.A
REARATTACHMENTPORT = port.E
TURNFACTOR = 1.66

#####################################################################
# Method to convert distance from inch to rotation degrees on motor
#####################################################################
def convertcmToDegree(cm):
    return int(360/( ROTATION_TO_CM ) * cm )

#####################################################################
# convert actual degree to motor specification
#####################################################################
def turnDegree(angle):
    return int(( TURNFACTOR ) * angle )

#####################################################################
# perform rescue tower
#####################################################################
async def BoatThingy():
    await motor_pair.move_tank_for_degrees(0, turnDegree(25), 200, -200)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(23), 500 , 500)
    await motor.run_for_degrees(FRONTATTACMENTPORT,-150, 500)
    await motor_pair.move_tank_for_degrees(0, turnDegree(28), 200, -200)
    motor.run_for_degrees(FRONTATTACMENTPORT,100, 500)
    motor_pair.move_tank_for_degrees(0, convertcmToDegree(-15), 500 , 500)
    await motor.run_for_degrees(FRONTATTACMENTPORT,-100, 500)
    motor_pair.move_tank_for_degrees(0, turnDegree(-250), 200, -200)
    motor_pair.move_tank_for_degrees(0, convertcmToDegree(10), 500 , 500)
    

#####################################################################
# Main code
#####################################################################
async def main():
    # Set Motor pair1
    motor_pair.pair(motor_pair.PAIR_1, WHEELRIGHTPORT, WHEELLEFTPORT)
    await BoatThingy()

runloop.run(main())