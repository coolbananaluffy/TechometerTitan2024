#route 0
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


async def main():
    motor_pair.pair(motor_pair.PAIR_1, WHEELRIGHTPORT, WHEELLEFTPORT)

#await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-5),800 , 800)
    #Forward 30
        # write your code here



    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(40),400 , 400)
    #Left 1 degree
    await leftGyro(150, motor_pair.PAIR_1)
#Drop attachement
    await motor.run_for_degrees(FRONTATTACMENTPORT,120,200)

    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-650),1000 , 1000)

    #Left 20 degrees
#await leftGyro(250,motor_pair.PAIR_1)
# go forward 10 cm
'''
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(10), 500 , 500)
#turn right 25 degreees
    await rightGyro(-250,motor_pair.PAIR_1)
#Lift attachment
    await motor.run_for_degrees(REARATTACHMENTPORT,2500,200)

'''


runloop.run(main())
