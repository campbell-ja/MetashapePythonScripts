# This script created by Joseph Aaron Campbell - 10/2020
# this script references https://www.agisoft.com/forum/index.php?topic=10564.msg47949#msg47949
# Use this as a learning tool only.
# I am not responsible for any damage to data or hardware if the script is not properly utilized.
# Following Code tested and based on Metashape Pro 1.6.2 using Windows 10 Pro
"""
Avoid removing too many points, as it will destroy the alignment
Also, if you see ripple like effects in the data then you've iterated too many times

"""

""" 
# # # # # # # # # # # # # # # 
SET UP THE WORKING ENVIRONMENT 
# # # # # # # # # # # # # # # 
"""

import Metashape

"""create a reference to the current project"""
doc = Metashape.app.document
# create reference for list of chunks in project
chunkList = Metashape.app.document.chunks
# set reference to the currently selected chunk
activeChunk = Metashape.app.document.chunk

""" Duplicate Chunk to preserve original Alignment """
# create a reference to the original chunk name
activeChunk_label = activeChunk.label
# set the label (name) of the original alignment
activeChunk.label = str(activeChunk.label + "-Source")
# Duplicate the source chunk
activeChunk.copy()
# update reference for list of chunks in project
chunkList = Metashape.app.document.chunks
# set reference to the last chunk in list, assuming this is the most recent copied chunk
dupeChunk = Metashape.app.document.chunks[len(Metashape.app.document.chunks)-1]
# rename the new copied chunk to match the chunk naming structure
if dupeChunk in chunkList:
    dupeChunk.label = str(activeChunk_label) + "-Filtered"

"""Set up point cloud filter and Gradual Selection options and values"""
# create a reference to the point cloud, and filter method
selection = Metashape.PointCloud.Filter()
# create list of gradual selection filter options and their threshold values. set the values in variables above this.
# options = Metashape.PointCloud.Filter(.ReprojectionError,.ReconstructionUncertainty,.ImageCount,.ProjectionAccuracy)
filterOptions = \
    [
        [Metashape.PointCloud.Filter.ReconstructionUncertainty, 10],
        [Metashape.PointCloud.Filter.ProjectionAccuracy, 4.0],
        [Metashape.PointCloud.Filter.ProjectionAccuracy, 3.0],
    ]


""" Loop through gradual Selection list and 
apply filter, remove points, optimize cameras; 
update the reference pane settings in preparation for setting up scale bars;
repeat Reprojection Error selection until MAX error is less than 0.3
"""

for index, filterOption in enumerate(filterOptions):

    print("processing filter index " + str(index) + ", " + str(filterOption[0]))

    # only run if current filterOption is not reprojection error, otherwise skip ahead
    if filterOption[0] is not Metashape.PointCloud.Filter.ReprojectionError:
        # perform filter selection
        selection.init\
            (
                dupeChunk,
                criterion=filterOption[0]
            )
        # selects all points above the passed threshold value
        selection.selectPoints(filterOption[1])
        # remove selected/filtered points above the passed threshold value
        selection.removePoints(filterOption[1])
        # optimize cameras using basic settings
        dupeChunk.optimizeCameras\
        (
            fit_f=True,
            fit_cx=True,
            fit_cy=True,
            fit_b1=False,
            fit_b2=False,
            fit_k1=True,
            fit_k2=True,
            fit_k3=True,
            fit_k4=False,
            fit_p1=True,
            fit_p2=True,
            fit_corrections=False,
            adaptive_fitting=False,
            tiepoint_covariance=False
        )

""" update the reference pane settings to match CHI scale bar workflow """
# this is done right before processing reprojection error and creating scale bars.

# set 'Scale Bar Accuracy' to 0.0001
dupeChunk.scalebar_accuracy = 0.0001
# set 'Tie Point Accuracy' to 0.1
dupeChunk.tiepoint_accuracy = 0.1
# set 'Marker Projection Accuracy' to 0.1
dupeChunk.marker_projection_accuracy = 0.1

# Save
doc.save()















