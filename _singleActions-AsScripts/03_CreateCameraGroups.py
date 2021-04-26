# This script created by Joseph Aaron Campbell - 03/2021

""" Set up Working Environment """
# import Metashape library module
import Metashape
# create a reference to the current project via Document Class
doc = Metashape.app.document
# set reference for the currently active chunk
activeChunk = Metashape.app.document.chunk

""" Create new Camera Groups """
# create a camera group for each camera sensor focal length
# each sensor is found under the 'Camera Calibrations...' menu option
for sensor in activeChunk.sensors:
    # create a camera group for the current sensor focal length
    cameraGroup = activeChunk.addCameraGroup()
    # rename the group to match the sensor focal length
    cameraGroup.label = str(str(int(sensor.focal_length)) + " mm")
    # loop through cameras and move any camera with matching sensor focal_length to new camera group
    for camera in activeChunk.cameras:
        if camera.sensor.focal_length == sensor.focal_length:
            camera.group = cameraGroup

