import wpilib
from wpilib.command import Command
import subsystems
import robotmap

class RunGearOutake(Command):

    def __init__(self):
        super().__init__('Gear Outake')
        self.requires(subsystems.gearoutake)
        self.position = position

    def execute(self):
        if robotmap.buttonsList.openGearID.isPressed()
            subsystems.gearoutake.set(0.8)
        if robotmap.buttonsList.closeGearID.isPressed()
            subsystems.gearoutake.set(0.0)

    def isFinished(self):
        super().isFinished()

    def end(self):
        subsystems.gearoutake.set(0)
