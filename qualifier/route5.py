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
  #  await motor.run_for_degrees(REARATTACHMENTPORT,50,250)
    await motor_pair.move_tank_for_degrees(0,convertInchToDegree(-2), 400, 400)
    await motor_pair.move_tank_for_degrees(0,convertInchToDegree(10), 400, 400)

    await motor_pair.move_tank_for_degrees(0, turnDegree(-45), 200, -200)
    runloop.sleep_ms(1000)

    await motor_pair.move_tank_for_degrees(0,convertInchToDegree(12), 400, 400)

    await motor_pair.move_tank_for_degrees(0,convertInchToDegree(-4), 200, 200)
    await motor_pair.move_tank_for_degrees(0, turnDegree(-45), 200, -200)
    await motor_pair.move_tank_for_degrees(0,convertInchToDegree(5), 500, 500)
    await motor_pair.move_tank_for_degrees(0, turnDegree(42), 200, -200)
    await motor_pair.move_tank_for_degrees(0,convertInchToDegree(16), 1000, 1000)
    await motor_pair.move_tank_for_degrees(0, turnDegree(-15), 200, -200)
    await motor_pair.move_tank_for_degrees(0,convertInchToDegree(4), 1000, 1000)

    # end of angler fish
    await motor_pair.move_tank_for_degrees(0,convertInchToDegree(4), 1000, 1000)
    await motor_pair.move_tank_for_degrees(0, turnDegree(115), 500, -500)
    await motor.run_for_degrees(REARATTACHMENTPORT,-120,250)

#    await motor.run_for_degrees(REARATTACHMENTPORT,75,250)

    await motor_pair.move_tank_for_degrees(0,convertInchToDegree(3), 1000, 1000)
    await motor.run_for_degrees(REARATTACHMENTPORT,-120,250)
    await motor_pair.move_tank_for_degrees(0, turnDegree(-40), 500, -500)
    await motor.run_for_degrees(REARATTACHMENTPORT,400,250)
    runloop.sleep_ms(2000)
    await motor.run_for_degrees(REARATTACHMENTPORT,400,250)
    runloop.sleep_ms(2000)
    await motor.run_for_degrees(REARATTACHMENTPORT,400,1000)
#    await motor_pair.move_tank_for_degrees(0, turnDegree(40), 500, -500)


    await motor_pair.move_tank_for_degrees(0, turnDegree(210), 500, -500)
    await motor.run_for_degrees(REARATTACHMENTPORT,400,250)
    await motor_pair.move_tank_for_degrees(0,convertInchToDegree(6.5), 1000, 1000)
    await motor_pair.move_tank_for_degrees(0,convertInchToDegree(-2), 500, 500)
    await motor_pair.move_tank_for_degrees(0, turnDegree(-97.5), 500, -500)
    await motor_pair.move_tank_for_degrees(0,convertInchToDegree(20), 1000, 1000)
    await motor_pair.move_tank_for_degrees(0, turnDegree(-20), 500, -500)
    await motor_pair.move_tank_for_degrees(0,convertInchToDegree(25), 1000, 1000)
    await runloop.sleep_ms(5000)
    await motor_pair.move_tank_for_degrees(0,convertInchToDegree(-25), 1000, 1000)
    
runloop.run(main())
