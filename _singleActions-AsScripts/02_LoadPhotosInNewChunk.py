# This script created by Joseph Aaron Campbell - 03/2021

""" Set up Working Environment """
# import Metashape library module
import Metashape
# create a reference to the current project via Document Class
doc = Metashape.app.document

""" Prompt User to Select Images """
# create array/list of images via user input gui
images = Metashape.app.getOpenFileNames()

""" Create New Chunk and Rename It """
# create new chunk to avoid changing any currently existing chunks
newChunk = doc.addChunk()
# set new chunk as active chunk
Metashape.app.document.chunk = newChunk
# set a new reference for the new chunk
activeChunk = newChunk

"""Rename the New Active Chunk"""
# get full list of chunks
chunkList = doc.chunks
# rename the new chunk,but only if it exists
# also add the integer position in chunks list
# this ensures each time the script runs each chunk has a unique name.
if activeChunk in chunkList:
    activeChunk.label = 'pyChunk_' + str(len(chunkList)-1)

""" Add User Selected Photos to Active Chunk"""
# add images to chunk from array/list created earlier
activeChunk.addPhotos(images)



