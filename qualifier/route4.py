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

async def Sonar():
    #Move robot forward 34 centimeters
   # await motor_pair.move_tank_for_degrees(0, convertcmToDegree(34), 500, 500)
    #Turn robot right 90 degrees
    await motor_pair.move_tank_for_degrees(0, turnDegree(40), 50, -50)
    #drop attachment
    await motor.run_for_degrees(FRONTATTACMENTPORT, -200, 600)

    
    #Move robot forward 25.7 centimeters
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(25.7), 500, 500)

    #TURN AGAIN

    await motor_pair.move_tank_for_degrees(0, turnDegree(55), 50, -50)



    await motor.run_for_degrees(FRONTATTACMENTPORT, 500, 500)

    #Move robot backward 73 centimeters
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-20), 500, 500)
    '''
    #Turn robot right 120 degrees
    await motor_pair.move_tank_for_degrees(0, turnDegree(120), 200, -200)
    #Move robot forward 20 centimeters
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(20), 500, 500)
'''
async def main():
    # Set Motor pair1
    motor_pair.pair(motor_pair.PAIR_1, WHEELRIGHTPORT, WHEELLEFTPORT)
    await Sonar()
    #await test()

runloop.run(main())
