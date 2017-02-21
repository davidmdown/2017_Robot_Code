'''Note the RotateWhileMoving method constructor initializes the robot
average speed toward the peg and the rotational speed of the robot. 
The former is proportional to the rate at which that the robot moves
forward and the later is proportional to the rate at which the robot
rotates counter clockwise. If the input value of the robot average
speed is negative then the robot moves backward (as it is supposed to
do in the autonomous mode. If the rotational speed is positive then
the robot will rotate clockwise.'''

from wpilib.command import Command

import subsystems
#import operatorinput as oi

import robotmap

import math


class RotateWhileMoving(Command):

    def __init__(self):
        #super().__init__('Rotate')

        self.requires(subsystems.drivetrain)

        subsystems.drivetrain.frEncoder.reset()
        subsystems.drivetrain.flEncoder.reset()
        subsystems.drivetrain.brEncoder.reset()
        subsystems.drivetrain.blEncoder.reset()

        self.average_speed = auto_camera.average_speed
        self.rotate_speed = auto_camera.rotate_speed

       '''Initialize the flag finished which indicates whether the while loop of
       the execute method is is finished. The while loop runs until robot motion stops.'''
        
        self.finished = False

    def initialize(self):
        pass

    def execute(self):

        '''The flag_distance traveled will be
        monitored to determine if the robot has stopped moving,
        which will occur when it either strikes the gear mounting
        peg or another object on the playing field. We want to stop
        autonomous motion when this happens.'''

        '''We will do the camera guided movement in a while loop
        which will execute as long as the distance traveled (which
        will always be negative because we are backing up in
        autonmous) is less than a limit contained in the variable
        robotmap.auto_camera.zeroDistance'''

        distance_traveled = -1000.
        
        finished = False

        while distance_traveled < robotmap.auto_camera.zeroDistance:

            x_peg = '''This should be a call to a network tables method
                that gets from the table the table property (variable)
                which contains the x coordinate (measured in pixels) of
                of the gear mount peg location in the image. By x coordinate
                it is meant which of the pixel columns in the 640 column
                by 480 row image the estimated peg position is.'''

            y_peg = '''This should be a call to a network tables method
                that gets from the table the table property (variable)
                which contains the x coordinate (measured in pixels) of
                of the gear mount peg location in the image. By y coordinate
                it is meant which of the pixel rows in the 640 column
                by 480 row image the estimated peg position is.'''

            '''If x_peg is greater than zero the target is to the right of the
            robot (assuming a camera looking backward in the direction of robot
            motion) and the robot must turn clockwise to correct the error.
            Therefore, the executed turn speed must be negative'''

            if x_peg > 0
                turn_speed = -self.rotate_speed
            elif: x_peg < 0
                turn_speed = self.rotate_speed

            '''Set the speed of both front wheels to the average robot speed
            and increase the speed of the left rear wheel by the turn speed
            while decreasing the speed of the right rear wheel by the same
            amount. This keeps the average speed of all four wheels equal to the
            average speed.'''

            subsystems.drivetrain.frontLeftWheel.set(self.average_speed)
            subsystems.drivetrain.frontRighttWheel.set(self.average_speed)
            subsystems.drivetrain.rearLeftWheel.set(self.average_speed + turn_speed)
            subsystems.drivetrain.rearRighttWheel.set(self.average_speed - turn_speed)

            '''Get the compute the distance traveled. This must be less than
            robotmap.auto_camera.zeroDistance if the robot has not struck an
            obstacle and stopped'''

            flDist = subsystems.drivetrain.frontLeft.getDistance()
            frDist = subsystems.drivetrain.frontRight.getDistance()

            distance_traveled = (flDist + frDist)/2

            '''The robot has stopped if the distance traveled is greater than
            the expected negative distance contained in robotmap.auto_camera.zeroDistance.
            Test for this condition and set the flag finished accordingly'''

            if distance_traveled >= robotmap.auto_camera.zeroDistance:
                self.finished = True

    

    def end(self):
        subsystems.drivetrain.set(0, 0, 0, 0)

    def isFinished(self):
        if self.finished == True
            return True
        else
            return False
