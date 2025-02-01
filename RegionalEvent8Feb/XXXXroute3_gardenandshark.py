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

    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-5),800 , 800)
    #Forward 30
        # write your code here

    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(23),1000 , 1000)
    await rightGyro(-300, motor_pair.PAIR_1)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(32),200 , 200)

    await leftGyro(100, motor_pair.PAIR_1)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(25),200 , 200)
    # await leftGyro(220, motor_pair.PAIR_1)

    #await rightGyro(-22.5, motor_pair.PAIR_1)

    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(2), 500 , 500)
    await rightGyro(-70, motor_pair.PAIR_1)

    await motor.run_for_degrees(FRONTATTACMENTPORT,100,300)
    await motor.run_for_degrees(FRONTATTACMENTPORT,-75,1000)
    runloop.sleep_ms(1000)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-5), 500 , 500)
    await leftGyro(250, motor_pair.PAIR_1)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(12 ), 500 , 500)
    await rightGyro(-100, motor_pair.PAIR_1)
    await motor.run_for_degrees(FRONTATTACMENTPORT, 500 , 1000)
    await leftGyro(900, motor_pair.PAIR_1)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-6), 500 , 500)
    await motor.run_for_degrees(FRONTATTACMENTPORT, -100 , 1000)

    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(4), 500 , 500)


    await leftGyro(200, motor_pair.PAIR_1)

    await motor.run_for_degrees(FRONTATTACMENTPORT, 1000 , 1000)
    await motor.run_for_degrees(FRONTATTACMENTPORT, -1000 , 1000)
    await motor.run_for_degrees(FRONTATTACMENTPORT, 1000 , 1000)



    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-15), 500 , 500)
    await leftGyro(900, motor_pair.PAIR_1)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(100), 1000 , 1000)

runloop.run(main())
