# This script created by Joseph Aaron Campbell - 10/2020
# Use this as a learning tool only.
# I am not responsible for any damage to data or hardware if the script is not properly utilized.
# Following Code tested and based on Metashape Pro 1.6.2 using Windows 10 Pro

""" With Help from:
https://www.agisoft.com/forum/index.php?topic=11075.msg50002#msg50002
https://www.agisoft.com/forum/index.php?topic=3618.msg18952#msg18952
"""

import Metashape

"""create a reference to the current project"""
doc = Metashape.app.document
# set reference to the active chunk
activeChunk = Metashape.app.document.chunk

"""Detect Markers"""
# Detect Circular 12bit coded markers
# Coded target options: [CircularTarget12bit, CircularTarget14bit, CircularTarget16bit, CircularTarget20bit]
activeChunk.detectMarkers\
    (
        target_type=Metashape.TargetType.CircularTarget12bit,
        tolerance=25,
        filter_mask=False,
        inverted=False,
        noparity=False,
        maximum_residual=5,
        minimum_size=0,
        minimum_dist=5
    )

# Detect Cross non-coded markers
# Non-coded target options: [CircularTarget, CrossTarget]
activeChunk.detectMarkers\
    (
        target_type=Metashape.TargetType.CrossTarget,
        tolerance=25,
        filter_mask=False,
        inverted=False,
        noparity=False,
        maximum_residual=5,
        minimum_size=0,
        minimum_dist=5
    )

"""Remove Markers with less than X number of projections"""
for marker in activeChunk.markers:
    # if marker has less than 9 projections, remove from chunk
    if len(marker.projections) < 9:
        activeChunk.remove(marker)
        #print(" ^^^^ Removed: " + marker.label + " for having only " + str(len(marker.projections)) + " projections ^^^^ ")


"""Optimize Marker Error Per Camera"""
# print out the current projection count for each marker
for m in activeChunk.markers:
    print("Marker: " + m.label + " has " + str(len(m.projections)) + " projections")


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
        """print("marker is " + str(marker.label))
        print("camera is " + str(camera))
        print("marker position = " + str(position))
        print("proj = " + str(marker.projections[camera].coord))
        print("reproj = " + str(camera.project(position)))"""
        proj = marker.projections[camera].coord
        reproj = camera.project(position)
        error = (proj - reproj).norm()

        # remove markers with projection error greater than 0.5
        if error > 0.5:
            # set the current marker projection to none for current camera/marker combination
            marker.projections[camera] = None
            #print("**** Removed: " + str(marker) + " with error of : " + str(error) + " ****")

"""Remove Markers with less than X number of projections"""
for marker in activeChunk.markers:
    # if marker has less than 9 projections, remove from chunk
    if len(marker.projections) < 9:
        activeChunk.remove(marker)
        #print(" ^^^^ Removed: " + marker.label + " for having only " + str(len(marker.projections)) + " projections ^^^^ ")

# print out the adjusted projection count for each marker
for marker in activeChunk.markers:
    print("Marker: " + marker.label + " now has " + str(len(marker.projections)) + " projections")


# save
doc.save()
