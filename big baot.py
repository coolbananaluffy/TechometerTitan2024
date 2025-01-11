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




def GetDegreesForInches(inches):
    return int(360 / 7 * inches)


 
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
degree = GetDegreesForInches(11.11111)






#####################################################################
# gyro function to turn left
#####################################################################
async def leftGyro(turnDegree,motorPair):
    motion_sensor.reset_yaw(0)


    while motion_sensor.tilt_angles()[0] < turnDegree:
        motor_pair.move(motorPair,-100)
    motor_pair.stop(motorPair)




#####################################################################
# gyro function to turn right
#####################################################################
async def rightGyro(turnDegree,motorPair):
    motion_sensor.reset_yaw(0)


    while motion_sensor.tilt_angles()[0] > turnDegree:
        motor_pair.move(motorPair,100)
    motor_pair.stop(motorPair)




#####################################################################
# Main code
#####################################################################
async def main():
    # Set Motor pair1
    motor_pair.pair(motor_pair.PAIR_1, WHEELRIGHTPORT, WHEELLEFTPORT)


    motion_sensor.set_yaw_face(motion_sensor.FRONT) # set the yaw face for gyro

    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(50), 500, 500)
    i=0
    while i<(10):
        i=i+(1)
        await motor_pair.move_tank_for_degrees(0, convertcmToDegree(8.5), 500, 500)
        await leftGyro(55,motor_pair.PAIR_1) # turn left 45 degree
    await leftGyro(45,motor_pair.PAIR_1)



runloop.run(main())
