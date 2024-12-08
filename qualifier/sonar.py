import hub
import motor
import runloop
import motor_pair
from hub import port
from hub import motion_sensor\


ROTATION_TO_CM = 28
ROTATION_TO_INCH = 11
WHEELRIGHTPORT = port.F
WHEELLEFTPORT = port.B
FRONTATTACMENTPORT = port.A
REARATTACHMENTPORT = port.E
TURNFACTOR = 1.66


def convertcmToDegree(cm):
    return int(360/(ROTATION_TO_CM) * cm)


def convertInchToDegree(inch):
    return int((360/ROTATION_TO_INCH) * inch)


def turnDegree(angle):
    return int((TURNFACTOR) * angle)


async def plankton():
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-14), 500 , 500)
    await motor_pair.move_tank_for_degrees(0, turnDegree(95), 200, -200)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(8), 500 , 500)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-20), 500 , 500)
    await motor_pair.move_tank_for_degrees(0, turnDegree(75), 200, -200)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(70), 500 , 500)

async def Sonar():
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(10), 200 , 200)
    #runloop.sleep_ms(300)
    await motor_pair.move_tank_for_degrees(0, turnDegree(-15), 200, -200)
    #runloop.sleep_ms(250)        
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(70), 500 , 500)
    await motor_pair.move_tank_for_degrees(0, turnDegree(3), 200, -200)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(10), 500 , 500)
    #
    await motor.run_for_degrees(REARATTACHMENTPORT,400,500)
    await motor.run_for_degrees(REARATTACHMENTPORT,-2000,500)




    
    
async def main():
    # Set Motor pair1
    motor_pair.pair(motor_pair.PAIR_1, WHEELRIGHTPORT, WHEELLEFTPORT)
    await Sonar()
    await plankton()
    #await test()

runloop.run(main())
