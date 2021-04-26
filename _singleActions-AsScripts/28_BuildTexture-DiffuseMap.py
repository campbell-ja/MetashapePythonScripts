# This script created by Joseph Aaron Campbell - 10/2020

""" Set up Working Environment """
# import Metashape library module
import Metashape
# create a reference to the current project via Document Class
doc = Metashape.app.document
# set reference for the currently active chunk
activeChunk = Metashape.app.document.chunk
# set reference to texture size, aka the pixel dimension
SIZE = 8192

""" Determine if User Argument Overides Default Threshold Value"""
# If the script is run via the 'Run Script..' command in Metashape
# then the user may input the threshold value using the 'Arguments' field
# If no arguments were given, then use the provided Threshold value of 10
# Else, if user has given a value, then use that instead
if len(sys.argv) == 1:
    thresh = SIZE
else:
    thresh = float(sys.argv[1])

"""Build Texture"""
# Options: ['DiffuseMap', 'NormalMap', 'OcclusionMap']
activeChunk.buildTexture\
    (
        blending_mode=Metashape.MosaicBlending,
        texture_size=thresh,
        fill_holes=True,
        ghosting_filter=True,
        texture_type=Metashape.Model.DiffuseMap,
        transfer_texture=True
    )