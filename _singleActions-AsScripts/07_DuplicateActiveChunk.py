# This script created by Joseph Aaron Campbell - 10/2020

""" Set up Working Environment """
# import Metashape library module
import Metashape
# create a reference to the current project via Document Class
doc = Metashape.app.document
# set reference for the currently active chunk
activeChunk = Metashape.app.document.chunk

""" Duplicate Active Chunk to Preserve Original Alignment """
# create a reference to the original chunk name
activeChunk_label = activeChunk.label
# update the label (name) of the original alignment to indicate as source
activeChunk.label = str(activeChunk.label + "-Source")
# Duplicate the source chunk
activeChunk.copy()
# update reference for list of chunks in project
chunkList = Metashape.app.document.chunks
# set reference to the last chunk in list, assuming this is the most recent copied chunk
dupeChunk = Metashape.app.document.chunks[len(Metashape.app.document.chunks)-1]
# rename the new copied chunk to match the chunk naming structure
if dupeChunk in chunkList:
    dupeChunk.label = str(activeChunk_label) + "-Filtered"