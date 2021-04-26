# This script created by Joseph Aaron Campbell - 10/2020

""" With Help from Agisoft Forum @:
https://www.agisoft.com/forum/index.php?topic=12027.msg53791#msg53791
"""

""" Set up Working Environment """
# import Metashape library module
import Metashape
# create a reference to the current project via Document Class
doc = Metashape.app.document
# set reference for the currently active chunk
activeChunk = Metashape.app.document.chunk
#set reference for tolerance value for import mask function
THESHOLD = 25

""" Determine if User Argument Overides Default Threshold Value"""
# If the script is run via the 'Run Script..' command in Metashape
# then the user may input the threshold value using the 'Arguments' field
# If no arguments were given, then use the provided Threshold value of 10
# Else, if user has given a value, then use that instead
if len(sys.argv) == 1:
    thresh = THRESHOLD
else:
    thresh = float(sys.argv[1])

"""Import Masks"""
# import masks function using active 3D model as source for all cameras in chunk
activeChunk.importMasks\
    (
        path='{filename}_mask.png',
        source=Metashape.MaskSourceModel,
        operation=Metashape.MaskOperationReplacement,
        tolerance=thresh
    )