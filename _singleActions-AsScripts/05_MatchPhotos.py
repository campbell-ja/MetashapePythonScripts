# This script created by Joseph Aaron Campbell - 10/2020

""" Set up Working Environment """
# import Metashape library module
import Metashape
# create a reference to the current project via Document Class
doc = Metashape.app.document
# set reference for the currently active chunk
activeChunk = Metashape.app.document.chunk

""" Match Photos for Active Chunk """
# 'downscale' controls the quality level. Options are 0=Highest, 1=High, 2=Medium, 3=Low, 4=Lowest
# WARNING - downscale quality 0=Highest, up-scales the images x4. where 1=High uses the true pixel data.
# the settings here also determine the .alignCameras() method quality
activeChunk.matchPhotos\
    (
        downscale=1,
        generic_preselection=False,
        reference_preselection=True,
        reference_preselection_mode=Metashape.ReferencePreselectionSource,
        filter_mask=False,
        mask_tiepoints=False,
        keypoint_limit=100000,
        tiepoint_limit=25000,
        keep_keypoints=False,
        guided_matching=False,
        reset_matches=False,
        subdivide_task=True,
        workitem_size_cameras=20,
        workitem_size_pairs=80,
        max_workgroup_size=100
    )