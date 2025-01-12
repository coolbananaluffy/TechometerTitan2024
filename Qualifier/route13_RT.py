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

    #await motor_pair.move_tank_for_degrees(0, convertcmToDegree(5), 800 , 800)
    #await motor.run_for_degrees(FRONTATTACMENTPORT,100,250)
    #await motor_pair.move_tank_for_degrees(0, turnDegree(60), 200, -200)
    #await motor_pair.move_tank_for_degrees(0, convertcmToDegree(24), 800 , 800)
    #await motor_pair.move_tank_for_degrees(0, turnDegree(15), 200, -200)
    await motor.run_for_degrees(REARATTACHMENTPORT,90,250)    
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(50), 1000, 1000)    
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(11), 200, 200)
    await motor.run_for_degrees(REARATTACHMENTPORT,-150,250)
    runloop.sleep_ms(2000)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-70), 1000 , 1000)
    await light_matrix.write("slow")
    

runloop.run(main())
