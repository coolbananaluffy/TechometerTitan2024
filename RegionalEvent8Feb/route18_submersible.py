from hub import light_matrix, motion_sensor, port
import runloop
import motor_pair
#from app import display
import motor
import color_matrix

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
    await motor_pair.move_tank_for_degrees(0,convertcmToDegree(48), 500, 500)

    await motor_pair.move_tank_for_degrees(0, turnDegree(-47), 200, -200)
    runloop.sleep_ms(1000)

    await motor_pair.move_tank_for_degrees(0,convertcmToDegree(64.5), 500, 500)

    await motor.run_for_degrees(REARATTACHMENTPORT,-800,500)

    ### SUBMARINE done

    await motor_pair.move_tank_for_degrees(0,convertcmToDegree(-17), 500, 500)

    await motor_pair.move_tank_for_degrees(0, turnDegree(-47), 200, -200)

    await motor.run_for_degrees(REARATTACHMENTPORT,500,500)

    await motor_pair.move_tank_for_degrees(0,convertcmToDegree(38), 500, 500)
    ### ANGLER FISH DONE
    await motor_pair.move_tank_for_degrees(0,convertcmToDegree(-10), 500, 500)

    await motor_pair.move_tank_for_degrees(0, turnDegree(20), 200, -200)

    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(730), 500 , 500)
    await motor_pair.move_tank_for_degrees(0, turnDegree(-90), 200, -200)
    await motor_pair.move_tank_for_degrees(0,convertcmToDegree(50), 800, 800)



    '''
    ATTEMPTING TO PICK THE SEABED SAMPLE AFTER SUBMARINE
    await motor.run_for_degrees(REARATTACHMENTPORT,-40,1000)
    await motor_pair.move_tank_for_degrees(0, turnDegree(80), 100, -100)
    #runloop.sleep_ms(3000)
    await motor_pair.move_tank_for_degrees(0, turnDegree(270), 1000, -1000)
    #await motor_pair.move_tank_for_degrees(0, turnDegree(90), 1000, -1000)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(30), 500 , 500)
    await motor_pair.move_tank_for_degrees(0, turnDegree(-90), 1000, -1000)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(40), 500 , 500)
    #await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-3), 500 , 500)
    #await motor.run_for_degrees(REARATTACHMENTPORT, 100,1000)
    #await motor_pair.move_tank_for_degrees(0, turnDegree(-90), 100, -100)
    #await motor_pair.move_tank_for_degrees(0, convertcmToDegree(10), 500 , 500)
    '''
    '''
    #GO BACK HOME AFTER SUBMARINE
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(40), 500 , 500)
    await motor_pair.move_tank_for_degrees(0, turnDegree(-90), 100, -100)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(50), 500 , 500)
    '''

'''
    await motor.run_for_degrees(REARATTACHMENTPORT,1000,1000)

    await motor.run_for_degrees(REARATTACHMENTPORT,-65,1000)

    await motor_pair.move_tank_for_degrees(0, turnDegree(500), 1000, -1000)
'''



runloop.run(main())
