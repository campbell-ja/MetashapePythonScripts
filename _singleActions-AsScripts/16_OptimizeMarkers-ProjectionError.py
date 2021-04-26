# This script created by Joseph Aaron Campbell - 10/2020

""" With Help from Agisoft Forum @:
https://www.agisoft.com/forum/index.php?topic=11075.msg50002#msg50002
https://www.agisoft.com/forum/index.php?topic=3618.msg18952#msg18952
"""

""" Set up Working Environment """
# import Metashape library module
import Metashape
# create a reference to the current project via Document Class
doc = Metashape.app.document
# set reference for the currently active chunk
activeChunk = Metashape.app.document.chunk
# set reference for projection error value
THESHOLD = 0.5

""" Determine if User Argument Overides Default Threshold Value"""
# If the script is run via the 'Run Script..' command in Metashape
# then the user may input the threshold value using the 'Arguments' field
# If no arguments were given, then use the provided Threshold value of 10
# Else, if user has given a value, then use that instead
if len(sys.argv) == 1:
    thresh = THRESHOLD
else:
    thresh = float(sys.argv[1])

"""Print out the current projection count for each marker"""
for m in activeChunk.markers:
    print("Marker: " + m.label + " has " + str(len(m.projections)) + " projections")

"""Optimize Marker Error Per Camera"""
# for each marker in list of markers for active chunk, remove markers from each camera with error greater than 0.5
for marker in activeChunk.markers:
    # skip marker if it has no position
    if not marker.position:
        print(marker.label + " is not defined in 3D, skipping...")
        continue

    # reference the position of the marker
    position = marker.position

    # for each camera in the list of cameras for current marker
    for camera in marker.projections.keys():
        if not camera.transform:
            continue
        proj = marker.projections[camera].coord
        reproj = camera.project(position)
        error = (proj - reproj).norm()

        # remove markers with projection error greater than 0.5
        if error > thresh:
            # set the current marker projection to none for current camera/marker combination
            marker.projections[camera] = None

"""Print out the adjusted projection count for each marker"""
for marker in activeChunk.markers:
    print("Marker: " + marker.label + " now has " + str(len(marker.projections)) + " projections")
