'''Note the Rotate method constructor takes the input degrees.
This is the amount that the robot is to rotate in dewgrees
counter clockwise. If the input value of degrees is negative then
the robot will rotate in a clockwise direction by an amount equal
to the absolute value of degrees.'''


from wpilib.command import Command

import subsystems
import operatorinput as oi

import robotmap

import math


class Rotate(Command):

    def __init__(self, degrees):
        super().__init__('Rotate')

        self.requires(subsystems.drivetrain)

        subsystems.drivetrain.frEncoder.reset()
        subsystems.drivetrain.flEncoder.reset()
        subsystems.drivetrain.brEncoder.reset()
        subsystems.drivetrain.blEncoder.reset()

        self.degrees = degrees

    def initialize(self):
        pass

    def execute(self):
        if self.degrees >= 0:
            subsystems.drivetrain.rearLeftWheel.set(-.6)
            subsystems.drivetrain.rearRightWheel.set(.6)
        else:
            subsystems.drivetrain.rearLeftWheel.set(.6)
            subsystems.drivetrain.rearRightWheel.set(-.6)

    def end(self):
        subsystems.drivetrain.set(0, 0, 0, 0)

    def isFinished(self):
        leftDist = subsystems.drivetrain.backLeft.getDistance()
        rightDist = subsystems.drivetrain.backRight.getDistance()
        circ = robotmap.auto.wheelBaseDiameter * math.pi
        avgDeg = (((leftDist / circ) * 360) - ((rightDist / circ) * 360)) / 2
        
        if self.degrees <= 0:
            if avgDeg <= self.degrees:
                return True
            else:
                return False
        else:
            if avgDeg >= self.degrees:
                return True
            else:
                return False


