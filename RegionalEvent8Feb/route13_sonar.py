import hub
import motor
import runloop
import motor_pair
from hub import port
from hub import motion_sensor


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



async def Sonar():
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(55), 800 , 800)
    #runloop.sleep_ms(300)
    await motor_pair.move_tank_for_degrees(0, turnDegree(-32), 200, -200)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(33), 800 , 800)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(5), 800 , 800)
    await motor.run_for_degrees(FRONTATTACMENTPORT,300,1000)
    await motor.run_for_degrees(FRONTATTACMENTPORT,-1800,1000)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-8), 800 , 800)
    await motor_pair.move_tank_for_degrees(0, turnDegree(-60), 200, -200)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-40), 800 , 800)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(20), 800 , 800)
    await motor_pair.move_tank_for_degrees(0, turnDegree(-90), 200, -200)
    #await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-90), 800 , 800)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(60), 800 , 800)
    await motor_pair.move_tank_for_degrees(0, turnDegree(-100), 200, -200)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(30), 800 , 800)
"""
    #runloop.sleep_ms(250)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(70), 500 , 500)
    await motor_pair.move_tank_for_degrees(0, turnDegree(3), 200, -200)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(10), 500 , 500)
    #
    await motor.run_for_degrees(REARATTACHMENTPORT,400,500)
    await motor.run_for_degrees(REARATTACHMENTPORT,-2000,500)
"""





async def main():
    # Set Motor pair1
    motor_pair.pair(motor_pair.PAIR_1, WHEELRIGHTPORT, WHEELLEFTPORT)
    await Sonar()
    #await test()

runloop.run(main())
