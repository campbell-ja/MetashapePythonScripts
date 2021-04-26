# This script created by Joseph Aaron Campbell - 10/2020

""" Set up Working Environment """
# import Metashape library module
import Metashape
# create a reference to the current project via Document Class
doc = Metashape.app.document
# set reference for the currently active chunk
activeChunk = Metashape.app.document.chunk

""" Setup the Storage Environment """
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
outputSubfolder = Path(str(outputChunkFolder) + "\\" + "_Models")

print("output folder: " + str(outputFolder))
print("output chunk folder: " + str(outputChunkFolder))
print("model output folder is: " + str(outputSubfolder))

# create an 'output' sub-folder for exported data from project
# also create sub-folder for model export within 'output' sub-folder
# this method will create the folder if doesnt exist, and also do nothing if it does exist
Path(outputFolder).mkdir(exist_ok=True)
Path(outputChunkFolder).mkdir(exist_ok=True)
Path(outputSubfolder).mkdir(exist_ok=True)

"""Export the Dense Point Cloud"""
# set reference to the output filename and path for point cloud
outputFileName = str(str(outputSubfolder) + "\\" + str(activeChunk.label) + "_DENSECLOUD.ply")

# export dense point cloud
activeChunk.exportPoints\
    (
        path=outputFileName,
        source_data=Metashape.DenseCloudData,
        binary=True,
        save_normals=True,
        save_colors=True,
        save_classes=True,
        save_confidence=True,
        raster_transform=Metashape.RasterTransformNone,
        colors_rgb_8bit=True,
        comment="Exported Dense Point Cloud",
        save_comment=True,
        format=Metashape.PointsFormatPLY,
        image_format=Metashape.ImageFormatJPEG,
        clip_to_boundary=True,
        block_width=1000,
        block_height=1000,
        split_in_blocks=False,
        save_images=False,
        subdivide_task=True
    )