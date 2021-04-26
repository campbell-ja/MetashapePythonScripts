# This script created by Joseph Aaron Campbell - 10/2020

""" Set up Working Environment """
# import Metashape library module
import Metashape
# create a reference to the current project via Document Class
doc = Metashape.app.document
# set reference for the currently active chunk
activeChunk = Metashape.app.document.chunk
# set reference to custom face count
FACE_COUNT = 200000

""" Determine if User Argument Overides Default Threshold Value"""
# If the script is run via the 'Run Script..' command in Metashape
# then the user may input the threshold value using the 'Arguments' field
# If no arguments were given, then use the provided Threshold value of 10
# Else, if user has given a value, then use that instead
if len(sys.argv) == 1:
    thresh = FACE_COUNT
else:
    thresh = float(sys.argv[1])

"""Build Model Process"""
# must include this line between each attempt to build a model. or it overwrites last created model
activeChunk.model = None
# build model with custom face count
activeChunk.buildModel \
    (
        surface_type=Metashape.Arbitrary,
        interpolation=Metashape.EnabledInterpolation,
        face_count=Metashape.FaceCount.CustomFaceCount,
        face_count_custom=thresh,
        source_data=Metashape.DepthMapsData,
        vertex_colors=True,
        vertex_confidence=True,
        volumetric_masks=False,
        keep_depth=True,
        trimming_radius=10,
        subdivide_task=True,
        workitem_size_cameras=20,
        max_workgroup_size=100
    )