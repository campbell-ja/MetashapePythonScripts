# This script created by Joseph Aaron Campbell - 10/2020

""" Set up Working Environment """
# import Metashape library module
import Metashape
# create a reference to the current project via Document Class
doc = Metashape.app.document
# set reference for the currently active chunk
activeChunk = Metashape.app.document.chunk
# set reference for projection value
THRESHOLD = 9

""" Determine if User Argument Overides Default Threshold Value"""
# If the script is run via the 'Run Script..' command in Metashape
# then the user may input the threshold value using the 'Arguments' field
# If no arguments were given, then use the provided Threshold value of 10
# Else, if user has given a value, then use that instead
if len(sys.argv) == 1:
    thresh = THRESHOLD
else:
    thresh = float(sys.argv[1])


"""Remove Markers with less than X number of projections"""
for marker in activeChunk.markers:
    # if marker has less than 9 projections, remove from chunk
    if len(marker.projections) < thresh:
        activeChunk.remove(marker)


