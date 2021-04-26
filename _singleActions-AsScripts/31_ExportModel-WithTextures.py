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

"""Export the Model with Texture"""
# select the current model in the loop as the active model
model = activeChunk.model

# set reference to the output filename and path for 3D model and texture
outputFileName = str(str(outputSubfolder) + "\\" + str(model.label) + ".obj")

# export the 3D model
activeChunk.exportModel\
    (
        path=outputFileName,
        binary=True,
        precision=6,
        texture_format=Metashape.ImageFormatTIFF,
        save_texture=True,
        save_uv=True,
        save_normals=True,
        save_colors=True,
        save_cameras=True,
        save_markers=True,
        save_udim=False,
        save_alpha=False,
        strip_extensions=False,
        raster_transform=Metashape.RasterTransformNone,
        colors_rgb_8bit=True,
        comment="Created via Metashape python",
        save_comment=True,
        format=Metashape.ModelFormatOBJ,
    )