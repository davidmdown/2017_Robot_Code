
#Important Note: IN AUTONOMOUS MODE THE ROBOT MOVES BACKWARD

from wpilib.command.commandgroup import CommandGroup
from wpilib.command.waitcommand import WaitCommand

from .move import Move
from .rotate import Rotate

from commands.gear.opengear import OpenGear

import robotmap

class AutonomousCamera(CommandGroup):

    def __init__(self,start_position):
        super().__init__('Autonomous Program')

        self.requires(subsystems.drivetrain)

        '''Create a sequential command group for the camera autonomous
        mode'''

        '''Begin the command group with a deterministic move backward
        to the point where vision guidance will take over. If we are
        starting on the right or left side of the field, this initial
        move must be followed by a turn to the left or right. If we are
        in the center of the playing field a following turn is not
        necessary'''

        if start_position == 'right' OR start_position == 'left':
            self.addSequential(Move(robotmap.auto.initialDriveSide))
            if start_position == 'right':
                self.addSequential(Rotate(-60))
            else:
                self.addSequential(Rotate(60))
        else:
            self.addSequential(Move(robotmap.auto.initialDriveCenter))


        '''Now add to the sequential command group the command to rotate
        while moving. This moves the robot forward while images are taken
        with the camera to determine a turning direction. The ccommand finishes
        when the forward motion of the robot stops due to hitting an obstacle'''

        self.addSequential(RotateWhileMoving())

        '''If we have stopped then it's time to let go of the gear'''
        
        self.addSequential(OpenGear())
        self.addSequential(WaitCommand(1))

        '''Now it's time to back away from the peg'''
        
        self.addSequential(Move(robotmap.auto.stageThreeDrive))

        

        

