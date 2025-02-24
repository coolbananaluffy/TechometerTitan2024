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

async def main():
    motor_pair.pair(motor_pair.PAIR_1, WHEELRIGHTPORT, WHEELLEFTPORT)
    await motor.run_for_degrees(FRONTATTACMENTPORT,500,500)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(38), 500 , 500)
    await motor_pair.move_tank_for_degrees(0, turnDegree( 35 ), 200,-200)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(12), 500 , 500)
    await motor_pair.move_tank_for_degrees(0, turnDegree( 75 ), 200,-200)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-20), 500 , 500)
    await motor_pair.move_tank_for_degrees(0, turnDegree( 90 ), 200,-200)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-20), 500 , 500)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(45), 500 , 500)    
runloop.run(main())

