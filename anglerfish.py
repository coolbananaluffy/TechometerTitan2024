from hub import light_matrix, motion_sensor, port
import runloop
import motor_pair
from app import display
import motor

# declare constants
ROTATION_TO_CM = 28 #17.2787595947
ROTATION_TO_INCH = 11 #7
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
# convert distance from inch to rotation degrees on motor
#####################################################################
def convertInchToDegree(inch):
    return int ( ( 360 / ROTATION_TO_INCH ) * inch)
#####################################################################
# convert actual degree to motor specification
#####################################################################
def turnDegree(angle):
    return int(( TURNFACTOR ) * angle )



#####################################################################
# Main code
#####################################################################
async def main():
    # Set Motor pair1
    motor_pair.pair(motor_pair.PAIR_1, WHEELRIGHTPORT, WHEELLEFTPORT)

    await motor_pair.move_tank_for_degrees(0,convertInchToDegree(10), 1000, 1000)

    await motor_pair.move_tank_for_degrees(0, turnDegree(-45), 200, -200)
    runloop.sleep_ms(1000)
    
    await motor_pair.move_tank_for_degrees(0,convertInchToDegree(12), 500, 500)

    await motor_pair.move_tank_for_degrees(0,convertInchToDegree(-4), 500, 500)

    await motor_pair.move_tank_for_degrees(0, turnDegree(-45), 200, -200)
    runloop.sleep_ms(1000)

    await motor_pair.move_tank_for_degrees(0,convertInchToDegree(7), 500, 500)

    await motor_pair.move_tank_for_degrees(0, turnDegree(42), 200, -200)
    runloop.sleep_ms(1000)

    await motor_pair.move_tank_for_degrees(0,convertInchToDegree(20), 1000, 1000)
runloop.run(main())
