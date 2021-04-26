# This script created by Joseph Aaron Campbell - 10/2020
# Use this as a learning tool only.
# I am not responsible for any damage to data or hardware if the script is not properly utilized.
# Following Code tested and based on Metashape Pro 1.6.2 using Windows 10 Pro

""" # # # # # SET UP THE WORKING ENVIRONMENT # # # # # """

# import Metashape library module
import Metashape

# create a reference to the current project
# done via the Document Class
doc = Metashape.app.document

""" # # # # # START THE MAIN PIPELINE # # # # # """

""" ADD Photos to a new Chunk """
# create array/list of images via user input gui
images = Metashape.app.getOpenFileNames()

# create a new chunk
newChunk = doc.addChunk()

# get full list of chunks
chunkList = doc.chunks

# rename the new chunk,but only if it exists
# also add the integer position in chunks list
# this ensures each time the script runs each chunk has a unique name.
if newChunk in chunkList:
    newChunk.label = 'pyChunk_' + str(len(chunkList)-1)

# swap the reference for the currently active chunk
activeChunk = newChunk

# add images to chunk from array/list created earlier
activeChunk.addPhotos(images)

""" Create new Camera Groups """
# create a camera group for each camera sensor focal length
# each sensor is found under the 'Camera Calibrations...' menu option
# and is actually sorted and grouped by the lens and horizontal/vertical position of camera
for sensor in activeChunk.sensors:
    # create a camera group for the current sensor focal length
    cameraGroup = activeChunk.addCameraGroup()
    # rename the group to match the sensor focal length
    cameraGroup.label = str(str(int(sensor.focal_length)) + " mm")
    # loop through cameras and move any camera with matching sensor focal_length to new camera group
    for camera in activeChunk.cameras:
        if camera.sensor.focal_length == sensor.focal_length:
            camera.group = cameraGroup

# Estimate image quality
# this populates the 'Quality' column in the photos pane, under 'details' view
# this is not indicative of the actual image quality and is just here for example
activeChunk.analyzePhotos()

""" Save the Project """
# save document assuming the file has already been saved at least once.
# if the document has NOT been saved previously..
# then provide the path between the ().
doc.save()
