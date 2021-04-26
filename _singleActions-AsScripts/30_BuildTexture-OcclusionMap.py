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
# get the index value of the currently selected model relative to the chunk.models list
index = activeChunk.models.index(activeChunk.model)

# start, get the face count of the current model
currentFaceCount = [len(activeChunk.models[index].faces)]
# get the face count of the previous model in the list of models
previousFaceCount = [len(activeChunk.models[index-1].faces)]

# determine if the currently selected model has a lower face count than the previous model
# if the current model has a lower face count, then proceed to create the texture map
if currentFaceCount < previousFaceCount:
    # the source model is set to the index of the previously created model in the list of models.
    # this assumes that each subsequent model was created with a lower face count than the previous.
    # Options: ['DiffuseMap', 'NormalMap', 'OcclusionMap']
    activeChunk.buildTexture \
        (
            blending_mode=Metashape.MosaicBlending,
            texture_size=thresh,
            fill_holes=True,
            ghosting_filter=True,
            texture_type=Metashape.Model.OcclusionMap,
            source_model=activeChunk.models[index - 1],
            transfer_texture=True
        )
else:
    print(" PYTHON SCRIPT ERROR: Check face count of source model is more than the selected model ")

