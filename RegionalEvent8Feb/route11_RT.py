from hub import light_matrix, motion_sensor, port, sound
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
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(50), 1000, 1000)    
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(9), 200, 200)
    await motor.run_for_degrees(REARATTACHMENTPORT,-60,100)
    #await motor_pair.move_tank_for_degrees(0, convertcmToDegree(4), 100, 100)
    runloop.sleep_ms(4000)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-70), 1000 , 1000)
    
    

runloop.run(main())
