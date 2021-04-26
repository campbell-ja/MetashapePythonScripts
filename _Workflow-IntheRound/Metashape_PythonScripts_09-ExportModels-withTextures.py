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


""" # # # # # START THE MAIN PIPELINE # # # # # """

"""Export Model Process """
# export Wavefront .OBJ model(s)
# the model is named after its label (name)
# Hi-Res models are saved with .TIFF texture files.
# Low-Res models are saved with .JPEG texture files

# loop through the available models for this chunk and export
for model in activeChunk.models:
    # select the current model in the loop as the active model
    activeChunk.model = model
    # get the face count for current model in loop
    modelFaceCount = len(model.faces)
    # set reference to the output filename and path for 3D model and texture
    outputFileName = str(str(outputSubfolder) + "\\" + str(model.label) + ".obj")
    print("model output folder and name is : " + outputFileName)

    # if model has more than X number of faces, then save texture as tiff on export
    # else if model has less than X number of faces, then save texture as JPEG.
    if modelFaceCount > 300000:
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
    else:
        activeChunk.exportModel \
        (
            path=outputFileName,
            binary=True,
            precision=6,
            texture_format=Metashape.ImageFormatJPEG,
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

""" Save the Project """
# save document assuming the file has already been saved at least once.
# if the document has NOT been saved previously..
# then provide the path between the ().
doc.save()