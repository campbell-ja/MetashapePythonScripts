# This script created by Joseph Aaron Campbell - 10/2020

""" Set up Working Environment """
# import Metashape library module
import Metashape
# create a reference to the current project via Document Class
doc = Metashape.app.document
# set reference for the currently active chunk
activeChunk = Metashape.app.document.chunk
# set reference to slider threshold value in percentage, for the Reprojection Filter
THRESHOLD = 10

""" Set up Point Cloud Filter and Gradual Selection Options """
# create a reference to the point cloud, and filter method
point_filter = Metashape.PointCloud.Filter()

""" Initialize the Filter """
# perform filter selection
point_filter.init \
    (
        activeChunk,
        criterion=Metashape.PointCloud.Filter.ReprojectionError
    )

""" Determine if User Argument Overides Default Threshold Value"""
# If the script is run via the 'Run Script..' command in Metashape
# then the user may input the threshold value using the 'Arguments' field
# If no arguments were given, then use the provided Threshold value of 4
# Else, if user has given a value, then use that instead
if len(sys.argv) == 1:
    thresh = THRESHOLD
else:
    thresh = float(sys.argv[1])

""" Calculate Filter Slider Value that Equals 10% of Points"""
# copy the point cloud filter values into new variable
filterValues = point_filter.values.copy()
# sort the point cloud filter values so points with highest error are selected
filterValues.sort()
# find relative slider value that gives 10 percent of points
thresh10 = filterValues[int(len(filterValues) * (1 - thresh / 100))]

""" Select Points"""
# selects all points above the passed threshold value
point_filter.selectPoints(thresh10)

""" Check if Selected Points are more than Half of Point Cloud """
# use list comprehension to get total number of selected points
nselected = len([p for p in activeChunk.point_cloud.points if p.selected])

""" Set Reference Value for Half of Point Cloud """
half_points = (len(activeChunk.point_cloud.points)/2)

""" Remove Selected Points -But Only Up to Half of Point Cloud """
if nselected < half_points:
    # remove selected/filtered points above the passed threshold value
    point_filter.removePoints(thresh10)
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
