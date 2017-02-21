from types import SimpleNamespace

stateList = SimpleNamespace()
stateList.fourWheelDrive = True  # False if Mecanum

portsList = SimpleNamespace()

portsList.stickID = 0

portsList.rearRightWheelID = 0
portsList.frontLeftWheelID = 1
portsList.rearLeftWheelID = 2
portsList.frontRightWheelID = 3

portsList.ropeMotorID = 4

portsList.gearDoorID = 5

portsList.fuelOutakeMotorID = 6

buttonsAndAxesList = SimpleNamespace()

buttonsAndAxesList.startFuelOutakeID = 1
buttonsAndAxesList.stopFuelOutakeID = 2

buttonsAndAxesList.openGearID = 6
buttonsAndAxesList.closeGearID = 5

buttonsAndAxesList.rope60PercentID = 3
buttonsAndAxesList.rope100PercentID = 4

buttonsAndAxesList.ropeAxis = 4

positionList = SimpleNamespace()
positionList.closeGearDoorPosition = 0.0
positionList.openGearDoorPosition = 1.0

speedsList = SimpleNamespace()
speedsList.ropeSpeed = 0.9
speedsList.fuelOutakeSpeed = 0.9
speedsList.deadZoneRadius = 0.1
speedsList.minimumWheelRotation = 0.2

encoders = SimpleNamespace()
encoders.fr = [0, 1]
encoders.fl = [2, 3]
encoders.br = [4, 5]
encoders.bl = [6, 7]

encoders.distancePerPulse = 0.01745329251

auto = SimpleNamespace()

auto.initialDriveSide = -119.69
auto.initialDriveCenter = -103.8
auto.stageTwoDrive = -21.29
auto.stageThreeDrive = 12

auto.wheelBaseDiameter = 21.5

'''Create robotmap entries for autonomous_camera mode'''

'''Create a distance that is essentially zero distance traveled'''

auto_camera.zeroDistance = -10

'''Create an average speed for the autonomous_camera mode.
A negative average speed moves the robot toward the peg. A
negative rotate speed turns the robot counter clockwise'''

auto_camera.average_speed = -0.2
auto_camera.rotate_speed = -0.1

