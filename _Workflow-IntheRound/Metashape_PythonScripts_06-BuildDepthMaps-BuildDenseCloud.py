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

# set reference to the currently selected chunk
activeChunk = Metashape.app.document.chunk


""" # # # # # START THE MAIN PIPELINE # # # # # """

""" Build Dense Cloud Process"""
# build depth maps
# downscale = # 1=UltraHigh, 2=High, 4=Medium, 8=low
# Ultrahigh setting loads the image data at full resolution, High downsamples x2, medium downsamples x4, low x8
activeChunk.buildDepthMaps\
(
    downscale=1,
    filter_mode=Metashape.AggressiveFiltering,
    reuse_depth=False,
    max_neighbors=-1,
    subdivide_task=True,
    workitem_size_cameras=20,
    max_workgroup_size=100
)

# save now in case the machine freezes up during dense cloud processing. then re-use depth maps upon restart
doc.save()

# build dense cloud
# the quality of the dense cloud is determined by the quality of the depth maps
# "max_neighbors" value of '-1' will evaluate ALL IMAGES in parallel. 200-300 is good when there is a lot of image overlap.
# setting this value will fix an issue where there is excessive 'fuzz' in the dense cloud. the default value is 100.
activeChunk.buildDenseCloud\
(
    point_colors=True,
    point_confidence=True,
    keep_depth=True,
    max_neighbors=300,
    subdivide_task=True,
    workitem_size_cameras=20,
    max_workgroup_size=100
)

""" Save the Project """
# save document assuming the file has already been saved at least once.
# if the document has NOT been saved previously..
# then provide the path between the ().
doc.save()

