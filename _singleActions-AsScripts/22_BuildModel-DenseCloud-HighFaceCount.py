# This script created by Joseph Aaron Campbell - 10/2020

""" Set up Working Environment """
# import Metashape library module
import Metashape
# create a reference to the current project via Document Class
doc = Metashape.app.document
# set reference for the currently active chunk
activeChunk = Metashape.app.document.chunk

"""Build Model Process"""
# must include this line between each attempt to build a model. or it overwrites last created model
activeChunk.model = None
# build model with high face count
activeChunk.buildModel \
    (
        surface_type=Metashape.Arbitrary,
        interpolation=Metashape.EnabledInterpolation,
        face_count=Metashape.FaceCount.HighFaceCount,
        face_count_custom=200000,
        source_data=Metashape.DenseCloudData,
        vertex_colors=True,
        vertex_confidence=True,
        volumetric_masks=False,
        keep_depth=True,
        trimming_radius=10,
        subdivide_task=True,
        workitem_size_cameras=20,
        max_workgroup_size=100
    )