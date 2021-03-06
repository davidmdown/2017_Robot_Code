from wpilib.command import Command

import subsystems

import operatorinput as oi

import robotmap


class FollowJoystick(Command):

    def __init__(self):
        super().__init__('Follow Joystick')
        self.requires(subsystems.drivetrain)
        self.requires(subsystems.rope)

    def execute(self):
        x = oi.joystick.getX()
        y = oi.joystick.getY()
        z = oi.joystick.getZ()

        if x >= 0:
            xValue = robotmap.speedsList.minimumWheelRotation + \
                (1 - robotmap.speedsList.minimumWheelRotation) * (x ** 3)
        else:
            xValue = -1 * robotmap.speedsList.minimumWheelRotation + \
                (1 - robotmap.speedsList.minimumWheelRotation) * (x ** 3)

        if y >= 0:
            yValue = robotmap.speedsList.minimumWheelRotation + \
                (1 - robotmap.speedsList.minimumWheelRotation) * (y ** 3)
        else:
            yValue = -1 * robotmap.speedsList.minimumWheelRotation + \
                (1 - robotmap.speedsList.minimumWheelRotation) * (y ** 3)

        subsystems.drivetrain.set(xValue, yValue, z, 0)

        if oi.joystick.getRawButton(
                robotmap.buttonsAndAxesList.rope60PercentID):
            subsystems.rope.set(0.6)
        elif oi.joystick.getRawButton(robotmap.buttonsAndAxesList.rope100PercentID):
            subsystems.rope.set(1)
        else:
            value = oi.joystick.getRawAxis(
                robotmap.buttonsAndAxesList.ropeAxis) ** 3
            subsystems.rope.set(value)

    def end(self):
        subsystems.drivetrain.set(0, 0, 0, 0)

    def isFinished(self):
        return super().isFinished()
