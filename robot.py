import wpilib
from commandbased import CommandBasedRobot

import subsystems

from commands.autonomous.autonomous import Autonomous
from commands.gear.closegear import CloseGear

import operatorinput

import robotmap

'''import network tables in order to setup network tables for
communicating with camera process'''

from networktables import NetworkTables

# NetworkTables.initialize(server='roborio-2036-frc.local')


class Robot(CommandBasedRobot):
    """Robot program base framework.

    Overridden init and periodic methods are called at appropriate
    times automatically.
    """

    def robotInit(self):
        """Robot initiializer. Initializes things such as all of the subsystems
        and operator input objects.

        Runs once during startup.
        """
        subsystems.init()
        operatorinput.init()

        self.autonomous = Autonomous()

        """Launch the child process for obtaining centroids of the
        vision targets. See the documentation in camera.py and at
        http://robotpy.readthedocs.io/en/stable/vision/roborio.html"""

        wpilib.CameraServer.launch('camera.py:main')

        print("Initialized robot")

    def autonomousInit(self):
        """Prepares the code for the autonomous period.
        """
        CloseGear().start()

        self.autonomous.start()

        print("Autonomous initialized")

    def autonomousPeriodic(self):
        """Periodic code for the autonomous period.

        Called every 20ms or so.
        """
        wpilib.command.Scheduler.getInstance().run()

    def teleopInit(self):
        """Prepares the code for the tele-operated period.

        Runs once when remote control is activated
        """
        self.autonomous.cancel()

        print("Tele-op initialized.")

    def teleopPeriodic(self):
        """Periodic code for the tele-operated period.

        Called every 20ms or so.
        """
        wpilib.command.Scheduler.getInstance().run()

if __name__ == '__main__':
    wpilib.run(Robot)
