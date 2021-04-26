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

""" Build Model Process """
# create array of desired face count quality for models
# Options:['HighFaceCount','MediumFaceCount','LowFaceCount','CustomFaceCount']
modelQuality = [Metashape.FaceCount.HighFaceCount]

# set the desired face counts and respective model name (label) for each decimated model
targetModel = [[0, "_DefaultFaceCount"], [8000001,"_MASTER"], [1000001,"_RENDER"], [500001,"_PRINT"], [200001,"_WEB"]]

# build the hi-res model , or build a model for each model quality in modelQuality list above
# providing the 'num' index value via the enumerate() method
for num, qual in enumerate(modelQuality):
    # must include this line between each attempt to build a model. or it overwrites last created model
    activeChunk.model = None
    # build model for current face count quality level in array modelQuality via i
    activeChunk.buildModel\
        (
            surface_type=Metashape.Arbitrary,
            interpolation=Metashape.EnabledInterpolation,
            face_count=qual,
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
    # update the label (aka name) for the model using the index 'num'
    activeChunk.models[num].label = str(activeChunk.label) + str(targetModel[0][1])

# get the face count for hi-res model, assuming its the first model in the list 'models'
modelFaceCount = [len(activeChunk.models[0].faces)]

""" Decimate Hi-Res Model to create derivatives """
# create index to iterate through available models. this needs to be manual as the number of models will be unknown
index = 0
# iterate through the target models list, starting at index one. skipping the hi-res option
for fCount in targetModel[1:]:
    print("current ModelFaceCount is: " + str(modelFaceCount))
    print("target fCount[0] is: " + str(fCount[0]))
    print("loop index is: " + str(index))

    # if the current model face count is less than decimate target goal, then skip decimation
    if modelFaceCount[index] < fCount[0]:
        continue

    # if the current face count is greater than the target face count, then proceed
    if modelFaceCount[index] >= fCount[0]:
        print("Decimating the Current Model")
        # must include this line between each attempt to create a model. or it overwrites last created model
        activeChunk.model = None
        # decimate the most recent model
        activeChunk.decimateModel\
        (
            face_count=fCount[0],
            asset=activeChunk.models[index]
        )
        # insert the new models face count into the modelFaceCount list
        modelFaceCount.append(len(activeChunk.models[index + 1].faces))
        #iterate to the next model now that we have created it
        index = index + 1


"""Rename the Models to match their intended usage"""
# get the difference between the length of the models list and target output list
diff = (len(targetModel) - len(activeChunk.models))

# loop through list of models and update the label
for val, model in enumerate(activeChunk.models):
    # rename the new model to match Face Count usage by calling the correct index in list targetModel[]
    # only change name IF not hi-res model, aka if index is One or greater
    if not (str(activeChunk.models[val].label))==(str(activeChunk.label) + "_DefaultFaceCount"):
        # update the model name(label), skipping the HighFaceCount Model
        # also add the difference between target models length and model count to account for skipped decimation
        model.label = str(activeChunk.label) + str(targetModel[(val+diff)][1])
        print("Naming model: " + str(model.label))
        print("val is: " + str(val))
        print("diff is: " + str(diff))

""" Save the Project """
# save document assuming the file has already been saved at least once.
# if the document has NOT been saved previously..
# then provide the path between the ().
doc.save()