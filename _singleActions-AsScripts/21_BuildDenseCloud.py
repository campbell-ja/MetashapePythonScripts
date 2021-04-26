# This script created by Joseph Aaron Campbell - 10/2020

""" Set up Working Environment """
# import Metashape library module
import Metashape
# create a reference to the current project via Document Class
doc = Metashape.app.document
# set reference for the currently active chunk
activeChunk = Metashape.app.document.chunk
#set reference for max neighbors value
THESHOLD = 300

""" Determine if User Argument Overides Default Threshold Value"""
# If the script is run via the 'Run Script..' command in Metashape
# then the user may input the threshold value using the 'Arguments' field
# If no arguments were given, then use the provided Threshold value of 10
# Else, if user has given a value, then use that instead
if len(sys.argv) == 1:
    thresh = THRESHOLD
else:
    thresh = float(sys.argv[1])

"""Build Dense Cloud"""
# the quality of the dense cloud is determined by the quality of the depth maps
# "max_neighbors" value of '-1' will evaluate ALL IMAGES in parallel.
# 200-300 is good when there is a lot of image overlap.
# setting this value will fix an issue where there is excessive 'fuzz' in the dense cloud.
# the default value is 100.
activeChunk.buildDenseCloud\
(
    point_colors=True,
    point_confidence=True,
    keep_depth=True,
    max_neighbors=thresh,
    subdivide_task=True,
    workitem_size_cameras=20,
    max_workgroup_size=100
)