# This script created by Joseph Aaron Campbell - 10/2020
# this script references https://www.agisoft.com/forum/index.php?topic=10564.msg47949#msg47949
# Use this as a learning tool only.
# I am not responsible for any damage to data or hardware if the script is not properly utilized.
# Following Code tested and based on Metashape Pro 1.6.2 using Windows 10 Pro
"""
Avoid removing too many points, as it will destroy the alignment
Also, if you see ripple like effects in the data then you've iterated too many times

"""

""" With Help from: 
https://www.agisoft.com/forum/index.php?topic=12725.msg56460#msg56460
"""

import Metashape

# import just the specific 'def' (function) from helper scripts
from Metashape_PythonScripts_helper_01_DisableLowCameraProjections import DisableCameras_WithLowProjections

"""create a reference to the current project"""
doc = Metashape.app.document
# create reference for list of chunks in project
chunkList = Metashape.app.document.chunks
# set reference to the currently selected
# chunk -- this should be the duplicated chunk from part-01
activeChunk = Metashape.app.document.chunk
# percentage values for selection
THRESHOLD = 10

# create a reference to the point cloud, and filter method
point_Filter = Metashape.PointCloud.Filter()
# initialize the filter for Reprojection Error
point_Filter.init\
    (
        activeChunk,
        criterion=Metashape.PointCloud.Filter.ReprojectionError
    )
# get the initial max RMS error value from the filter
max_error = point_Filter.max_value
# copy the point cloud filter values into new variable
filterValues = point_Filter.values.copy()
# sort the point cloud filter values
filterValues.sort()
# take 10 percent of points, with worst Reprojection Error, create value
thresh = filterValues[int(len(filterValues) * (1 - THRESHOLD / 100))]

# while the MAX RMS error is greater than 0.301, keep iterating reprojection error filter and selection
while max_error > 0.301:
    # selects all points above the passed threshold value
    point_Filter.selectPoints(thresh)
    # remove selected/filtered points above the passed threshold value
    point_Filter.removePoints(thresh)
    # optimize cameras using full settings
    activeChunk.optimizeCameras \
        (
            fit_f=True,
            fit_cx=True,
            fit_cy=True,
            fit_b1=True,
            fit_b2=True,
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
    # recreate a reference to the point cloud, and filter method
    point_Filter = Metashape.PointCloud.Filter()
    # re-initialize the filter for Reprojection Error
    point_Filter.init \
            (
            activeChunk,
            criterion=Metashape.PointCloud.Filter.ReprojectionError
        )
    # get the initial max RMS error value from the filter
    max_error = point_Filter.max_value
    # copy the point cloud filter values into new variable
    filterValues = point_Filter.values.copy()
    # sort the point cloud filter values
    filterValues.sort()
    # take 10 percent of points, with worst Reprojection Error, create value
    thresh = filterValues[int(len(filterValues) * (1 - THRESHOLD / 100))]
    print("MAX RMS ERROR IS: " + str(max_error))

""" disable cameras with low camera projections below 200
# but this only disables the lowest 10% of all cameras"""
DisableCameras_WithLowProjections(activeChunk)

""" reset region ( a.k.a reset the bounding box ) """
# hopefully, this will size the bounding box region proportional to the filtered point cloud
activeChunk.resetRegion()


# save the document
doc.save()













