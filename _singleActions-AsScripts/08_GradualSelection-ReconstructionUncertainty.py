# This script created by Joseph Aaron Campbell - 10/2020

""" Set up Working Environment """
# import Metashape library module
import Metashape, sys

# create a reference to the current project via Document Class
doc = Metashape.app.document
# set reference for the currently active chunk
activeChunk = Metashape.app.document.chunk
# set reference to slider threshold value for gradual selection filter
THRESHOLD = 10

""" Set up Point Cloud Filter and Gradual Selection Options """
# create a reference to the point cloud, and filter method
point_filter = Metashape.PointCloud.Filter()

""" Initialize the Filter and Select Points """
# perform filter selection
point_filter.init \
    (
        activeChunk,
        criterion=Metashape.PointCloud.Filter.ReconstructionUncertainty
    )

""" Determine if User Argument Overides Default Threshold Value"""
# If the script is run via the 'Run Script..' command in Metashape
# then the user may input the threshold value using the 'Arguments' field
# If no arguments were given, then use the provided Threshold value of 10
# Else, if user has given a value, then use that instead
if len(sys.argv) == 1:
    thresh = THRESHOLD
else:
    thresh = float(sys.argv[1])

# selects all points above the passed threshold value
point_filter.selectPoints(thresh)

""" Check if Selected Points are more than Half of Point Cloud """
# use list comprehension to get total number of selected points
nselected = len([p for p in activeChunk.point_cloud.points if p.selected])

""" Set Reference Value for Half of Point Cloud """
half_points = (len(activeChunk.point_cloud.points)/2)

""" Remove Selected Points -But Only Up to Half of Point Cloud """
if nselected < half_points:
    # remove selected/filtered points above the passed threshold value
    point_filter.removePoints(thresh)
else:
    # copy the current selection of points
    s_copy = point_filter.values.copy()
    # sort the copied values
    s_copy.sort()
    # get the threshold value for current filter, which gives 50% of points
    thresh50 = s_copy[int(len(s_copy) * 0.5)]
    # select 50% of point cloud using threshold
    point_filter.selectPoints(thresh50)
    # remove selected/filtered points
    point_filter.removePoints(thresh50)
