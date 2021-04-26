# This script created by Joseph Aaron Campbell - 10/2020
# this script references https://www.agisoft.com/forum/index.php?topic=10564.msg47949#msg47949
# Use this as a learning tool only.
# I am not responsible for any damage to data or hardware if the script is not properly utilized.
# Following Code tested and based on Metashape Pro 1.6.2 using Windows 10 Pro


""" With Help from: 
https://www.agisoft.com/forum/index.php?topic=12027.msg53791#msg53791
"""

""" 
# # # # # # # # # # # # # # # 
SET UP THE WORKING ENVIRONMENT 
# # # # # # # # # # # # # # # 
"""

import Metashape

"""create a reference to the current project"""
doc = Metashape.app.document
# create reference for list of chunks in project
chunkList = Metashape.app.document.chunks
# set reference to the currently selected chunk -- this should be the duplicated chunk from part-01
activeChunk = Metashape.app.document.chunk

# must include this line between each attempt to build a model. or it overwrites last created model
activeChunk.model = None
# using optimized sparse cloud, create lower resolution model
activeChunk.buildModel\
    (
        surface_type=Metashape.Arbitrary,
        interpolation=Metashape.EnabledInterpolation,
        face_count=Metashape.FaceCount.LowFaceCount,
        face_count_custom=200000,
        source_data=Metashape.PointCloudData,
        vertex_colors=True,
        vertex_confidence=True,
        volumetric_masks=False,
        keep_depth=True,
        trimming_radius=10,
        subdivide_task=True,
        workitem_size_cameras=20,
        max_workgroup_size=100
    )

# import masks function using lower resolution model as source for all cameras in chunk
activeChunk.importMasks\
    (
        path='{filename}_mask.png',
        source=Metashape.MaskSourceModel,
        operation=Metashape.MaskOperationReplacement,
        tolerance=10
    )


# get the current Chunks label ( name )
currentChunkLabel = activeChunk.label

# get the current (saved) project's parent folder URL via python3 pathLib
# this path variable is used when exporting the 3D model later in the script.
# 'parent' will return the parent folder the project lives in
# 'name' will return the saved project name and extension
# 'stem' will return just the project name without extension
from pathlib import Path
parentFolderPath = str(Path(Metashape.app.document.path).parent)
print("parent Folder is : " + parentFolderPath)

# set reference to the output folders as string
outputFolder = Path(str(parentFolderPath) + "\\" + "_Output")
outputChunkFolder = Path(str(outputFolder) + "\\" + "_" + str(currentChunkLabel))
outputMaskfolder = Path(str(outputChunkFolder) + "\\" + "_Masks")

print("output folder: " + str(outputFolder))
print("output chunk folder: " + str(outputChunkFolder))
print("model output folder is: " + str(outputMaskfolder))

# create an 'output' sub-folder for exported data from project
# also create sub-folder for model export within 'output' sub-folder
# this method will create the folder if doesnt exist, and also do nothing if it does exist
Path(outputFolder).mkdir(exist_ok=True)
Path(outputChunkFolder).mkdir(exist_ok=True)
Path(outputMaskfolder).mkdir(exist_ok=True)

# export masks to output mask folder
# this uses the Metashape Task class, otherwise loop through every camera in chunk and save mask as image file
# create a reference to the Tasks ExportMasks method
mask_task = Metashape.Tasks.ExportMasks()
# define which cameras to export masks for
mask_task.cameras = activeChunk.cameras
# define the output path for the exported mask files
mask_task.path = str(str(outputMaskfolder) + "\\" + "{filename}.png")
# activate the task for the active chunk to export the masks
mask_task.apply(object=activeChunk)

# delete lower resolution model
activeChunk.remove(activeChunk.models[0])

# save document
doc.save()