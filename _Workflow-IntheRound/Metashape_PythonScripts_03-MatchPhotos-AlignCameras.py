# This script created by Joseph Aaron Campbell - 10/2020
# Use this as a learning tool only.
# I am not responsible for any damage to data or hardware if the script is not properly utilized.
# Following Code tested and based on Metashape Pro 1.6.2 using Windows 10 Pro

""" # # # # # SET UP THE WORKING ENVIRONMENT # # # # # """


# import Metashape library module
import Metashape

# create a reference to the current project
# done via the Document Class
doc = Metashape.app.document

# set reference to currently selected chunk
activeChunk = Metashape.app.document.chunk


""" # # # # # START THE MAIN PIPELINE # # # # # """
# match photos for newest chunk
# 'downscale' controls the quality level. Options are 0=Highest, 1=High, 2=Medium, 3=Low, 4=Lowest
# WARNING - downscale quality 0=Highest, up-scales the images.
# the settings here also effect the .alignCameras() method
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

# align the matched image pairs
activeChunk.alignCameras()

""" Save the Project """
# save document assuming the file has already been saved at least once.
# if the document has NOT been saved previously..
# then provide the path between the ().
doc.save()
