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

""" Build Texture Process """
# create array of desired texture type for low-res models
# Options:n ['DiffuseMap', 'NormalMap', 'OcclusionMap']
textureType = [Metashape.Model.NormalMap, Metashape.Model.OcclusionMap]

# loop through each model and uv unwrap, then build texture.
for index, model in enumerate(activeChunk.models):
    # select the current model as the active model, as we iterate through the available models
    activeChunk.model = model
    # UV unwrap model
    activeChunk.buildUV\
    (
        mapping_mode=Metashape.GenericMapping,
        page_count=1,
        adaptive_resolution=False
    )
    # build higher resolution 8192k texture maps for both hi-res and MASTER 3D models
    # this assumes they are in the 0 and 1 position of the models list
    if index <= 1:
        # build diffuse texture map
        activeChunk.buildTexture\
            (
                blending_mode=Metashape.MosaicBlending,
                texture_size=8192,
                fill_holes=True,
                ghosting_filter=True,
                texture_type=Metashape.Model.DiffuseMap,
                transfer_texture=True
            )
    # build 4096k resolution texture maps for remaining models
    else:
        # build diffuse texture map
        activeChunk.buildTexture \
            (
                blending_mode=Metashape.MosaicBlending,
                texture_size=4096,
                fill_holes=True,
                ghosting_filter=True,
                texture_type=Metashape.Model.DiffuseMap,
                transfer_texture=True
            )

        # loop through textureType array and build texture for each texture type
        # source_model= determines which model to use for baking texture maps,
            # this uses the previous model quality to build the normal and diffuse map, to avoid errors in the maps from
            # using too high of a face count as a source for low poly meshes
        # Options: NormalMap(requires 2 models), Occlusion Map
        for tex in textureType:
            # you have to create the texture in memory before filling with data
            activeChunk.model.addTexture(tex)
            # build the texture, pulling the texture_type from the array with 't'
            activeChunk.buildTexture\
            (
                blending_mode=Metashape.MosaicBlending,
                texture_size=4096,
                fill_holes=True,
                ghosting_filter=True,
                texture_type=tex,
                source_model=activeChunk.models[index-1],
                transfer_texture=True
            )

""" Save the Project """
# save document assuming the file has already been saved at least once.
# if the document has NOT been saved previously..
# then provide the path between the ().
doc.save()
