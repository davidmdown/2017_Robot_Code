from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton

from commands.runintake import RunIntake

from commands.gear.closegear import CloseGear
from commands.gear.opengear import OpenGear

from commands.runoutput import RunOutput
from commands.runropeintake import RunRopeIntake

from commands.stopintake import StopIntake
from commands.stopoutput import StopOutput
from commands.stopropeintake import StopRopeIntake

import robotmap


joystick = None


def init():
    global joystick

    joystick = Joystick(robotmap.portsList.stickID)

    startIntakeButton = JoystickButton(
        joystick, robotmap.buttonsAndAxesList.startIntakeID)
    startIntakeButton.whenPressed(RunIntake(robotmap.speedsList.intakeSpeed))
    stopIntakeButton = JoystickButton(
        joystick, robotmap.buttonsAndAxesList.stopIntakeID)
    stopIntakeButton.whenPressed(StopIntake())

    startOutputButton = JoystickButton(
        joystick, robotmap.buttonsAndAxesList.startOutputID)
    startOutputButton.whenPressed(RunOutput(robotmap.speedsList.outputSpeed))
    stopOutputButton = JoystickButton(
        joystick, robotmap.buttonsAndAxesList.stopOutputID)
    stopOutputButton.whenPressed(StopOutput())

    openGearDoorButton = JoystickButton(
        joystick, robotmap.buttonsAndAxesList.openGearID)
    openGearDoorButton.whenPressed(
        OpenGear())
    closeGearDoorButton = JoystickButton(
        joystick, robotmap.buttonsAndAxesList.closeGearID)
    closeGearDoorButton.whenPressed(
        CloseGear())

    startRopeIntakeButton = JoystickButton(
        joystick, robotmap.buttonsAndAxesList.startRopeID)
    startRopeIntakeButton.whenPressed(
        RunRopeIntake(robotmap.speedsList.intakeSpeed))
    stopRopeIntakeButton = JoystickButton(
        joystick, robotmap.buttonsAndAxesList.stopRopeID)
    stopRopeIntakeButton.whenPressed(StopRopeIntake())
