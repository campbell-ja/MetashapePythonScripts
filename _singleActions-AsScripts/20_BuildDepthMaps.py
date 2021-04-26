# This script created by Joseph Aaron Campbell - 10/2020

""" Set up Working Environment """
# import Metashape library module
import Metashape
# create a reference to the current project via Document Class
doc = Metashape.app.document
# set reference for the currently active chunk
activeChunk = Metashape.app.document.chunk
#set reference for max neighbors value
THESHOLD = -1

""" Determine if User Argument Overides Default Threshold Value"""
# If the script is run via the 'Run Script..' command in Metashape
# then the user may input the threshold value using the 'Arguments' field
# If no arguments were given, then use the provided Threshold value of 10
# Else, if user has given a value, then use that instead
if len(sys.argv) == 1:
    thresh = THRESHOLD
else:
    thresh = float(sys.argv[1])

"""Build Depth Maps"""
# downscale = # 1=UltraHigh, 2=High, 4=Medium, 8=low
# Ultrahigh setting loads the image data at full resolution, High down-samples x2, medium down-samples x4, low x8
# the 'max_neighbors' determines how many cameras it compares in parallel. 100 is default value.
# setting 'max_neighbors' to -1 compares all cameras as same time.
activeChunk.buildDepthMaps\
(
    downscale=1,
    filter_mode=Metashape.AggressiveFiltering,
    reuse_depth=False,
    max_neighbors=thresh,
    subdivide_task=True,
    workitem_size_cameras=20,
    max_workgroup_size=100
)