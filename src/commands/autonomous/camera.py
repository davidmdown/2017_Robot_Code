#
#This is copied from http://robotpy.readthedocs.io/en/stable/vision/roborio.html
#
#Important Notes:
#
# - This is a file for a child process that acquires images
#   of the vision targets and processeses them to return thier
#   centroids. This code should not be imported into python robot code
#
# - This image processing code will be launched via a stub
#   that will setup logging and initialize pynetworktables
#   to talk to the robot code
#
# - The child process will NOT be launched when running the
#   robot code in simulation or unit testing mode
#
# - In the image processing code below, the code inside the
#   if __name__ == '__main__': will NOT be executed when the
#   code is launched from the robot code

import cv2
import numpy as np
import robotmap

from cscore import CameraServer

def main():
    
    cs = CameraServer.getInstance()
    cs.enableLogging()

    camera = cs.addAxisCamera(robotmap.network.camera)
    
    cs.startAutomaticCapture(camera = camera)
    
    camera.setResolution(640, 480)
    
    # Get a CvSink. This will capture images from the camera
    cvSink = cs.getVideo()
    
    # (optional) Setup a CvSource. This will send images back to the Dashboard
 #   outputStream = cs.putVideo("Rectangle", 640, 480)
    
    # Allocating new images is very expensive, always try to preallocate
    img = np.zeros(shape=(480, 640, 3), dtype=np.uint8)    

    while True:
        # Tell the CvSink to grab a frame from the camera and put it
        # in the source image.  If there is an error notify the output.
        time, img = cvSink.grabFrame(img)
        if time == 0:
            # Send the output the error.
            outputStream.notifyError(cvSink.getError());
            # skip the rest of the current iteration
            continue
        
        '''Insert image processing code here to calculate x_peg and
        y_peg, the x and y coordinates measured in pixels of the mid
        point between the computed centers of the two vision targets.
        By x coordinate it is meant which of the pixel columns in the
        640 column by 480 row image the estimated peg position is. By
        y coordinate it is meant which of the pixel rows in the 640
        column by 480 row image the estimated peg position is.'''

        x_peg = 0
        y_peg = 0

        '''Insert image processing code here to call a network tables
        method that puts the value in x_peg into the table property
        (variable) which contains the x coordinate and puts y_peg into
        the table property which contains the y coordinate.'''
        
        
        # (optional) Give the output stream a new image to display
 #      outputStream.putFrame(img)

if __name__ == '__main__':
    
    # To see messages from networktables, you must setup logging
    import logging
    logging.basicConfig(level=logging.DEBUG)
    
    # You should uncomment these to connect to the RoboRIO
    #import networktables
    #networktables.initialize(server='10.xx.xx.2')
    
    main()
