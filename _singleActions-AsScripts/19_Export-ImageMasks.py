# This script created by Joseph Aaron Campbell - 10/2020

""" With Help from Agisoft Forum @:
https://www.agisoft.com/forum/index.php?topic=12027.msg53791#msg53791
"""

""" Set up Working Environment """
# import Metashape library module
import Metashape
# create a reference to the current project via Document Class
doc = Metashape.app.document
# set reference for the currently active chunk
activeChunk = Metashape.app.document.chunk

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
print("mask output folder is: " + str(outputMaskfolder))

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

