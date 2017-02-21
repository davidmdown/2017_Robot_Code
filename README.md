Here is a list of the changes/additions I made:

Change to robot.py

  -added a statement to import NetworkTables from networktables
  
  -added a statement along with comment to launch the camera child process in the robotInit method
  
Change to robotmap.py

  -added a data attribute, auto_camera.zeroDistance, which contains an upper bound for the distance that the
   robot must move in order for it to be considered still moving while using camera guidance
   
  -added a data attribute, auto_camera.average_speed, that sets the average speed of the robot's 4 wheels
   during movment under camera guidance. The two front wheels always move at this speed. One of the back
   wheels moves at this speed minus the amount contained in auto_camera.rotate_speed and the other
   moves at this speed plus the amount contained in auto_camera.rotate_speed.
   
  -added the data attribute auto_camera.rotate_speed. See above for explanation
  
  -added the data attribute auto_camera.initialDriveCenter which contains an initial distance
   for the robot to move when executing autonomous_camera in the case where the robot is to place
   the gear on the center lift
   
Change to rotate.py

  - Added comment suggesting an interpretation of the input to the class constructor, degrees.
    This interpretation is that when degrees is positive then a counterclockwise rotation is 
    desired and when it is negative a clockwise rotation is desired. (This is in keeping with 
    standard interpretations of positive and negative rotations in physics and engineering.)
    
  - Modified the code for the isFinished method. When the input degrees is positive (counterclockwise
    rotation called for) leftDist should get more negative and rightDist should get more positive as
    the robot turns, and this means that avgDeg should get more positive. When avgDeg exceeds the 
    positive value in self.degrees the turn is finished.
    
Added autonomous_camera.py

  - This is based on autonomous.py. It constructs a command group using the addSequential method of
    the CommandGroup class. The first two commands in the command group move the robot to
    the position and orientation where camera guidance can be used for the next moves. 
    (Essentially we move the robot to where the vision targets used for camera guidance
    should be in the center of the camera field of view. The next command added to 
    the command group, RotateWhileMoving, moves the robot forward and simultaneously turns it. 
    The movement and turning commands occur within a While loop contained in RotateWhileMoving.
    This While loop is executed until the distance the robot moves during a loop iteration 
    (as determined by the encoders) is sufficiently small. This means the robot has stopped, 
    which must mean that it is pressing against the peg of the lift. The last three commands 
    added to the command group in autonomous_camera are identical to the last three commands 
    in the command group of autonomous. They command the gear housing to open, wait for it to
    open, and then move the robot back.
    
Added camera.py

 - This is code for the child process launched in robot.py that acquires images from the Axis
   camera and processes them to find the vision targets, find their centroids, find the midpoint
   between their centroids, put the x and y coordinates (in the variables x_peg and y_peg into
   the network tables so that they can be accessed by the command RotateWhileMoving
