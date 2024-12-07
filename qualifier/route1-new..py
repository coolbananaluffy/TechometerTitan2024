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
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(10), 800 , 800)
    await motor_pair.move_tank_for_degrees(0, turnDegree( 12 ), 200,-200)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(45), 800 , 800)
    await motor_pair.move_tank_for_degrees(0, turnDegree( 25 ), 200,-200)
    await motor_pair.move_tank_for_degrees(0, turnDegree( -25 ), 200,-200)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(15), 800 , 800)
    #krills 3,4 +coral 3 collected
    await motor_pair.move_tank_for_degrees(0, turnDegree( -12 ), 200,-200)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(10), 800 , 800)
    await motor.run_for_degrees(FRONTATTACMENTPORT, -45, 500)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(8), 800 , 800)
    await motor.run_for_degrees(FRONTATTACMENTPORT, -60, 500)
    await motor.run_for_degrees(FRONTATTACMENTPORT, 75, 500)
    # Move out after flipping corals
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-18), 800 , 800)
    await motor_pair.move_tank_for_degrees(0, turnDegree( -30 ), 200,-200)
    await motor.run_for_degrees(REARATTACHMENTPORT, -120, 500)
    # Whale released
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-24), 800 , 800)
    await motor_pair.move_tank_for_degrees(0, turnDegree( -120 ), 200,-200)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(40), 800 , 800)
    #await motor_pair.move_tank_for_degrees(0, convertcmToDegree(5), 800 , 800)
    '''
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-15), 400 , 400)
    await motor_pair.move_tank_for_degrees(0, turnDegree( 90 ), 200,-200)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(15), 800 , 800)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-28), 400 , 400)
    #fifth krill collected
    await motor_pair.move_tank_for_degrees(0, turnDegree( -20 ), 200,-200)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(18), 400 , 400)
    await motor_pair.move_tank_for_degrees(0, turnDegree( 60 ), 200,-200)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(13), 400 , 400)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-25), 400 , 400)
    #sample collected

    await motor_pair.move_tank_for_degrees(0, turnDegree( 90 ), 200,-200)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(55), 800 , 800)
    await motor_pair.move_tank_for_degrees(0, turnDegree( -90 ), 200,-200)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(20), 400 , 400)
    '''

runloop.run(main())