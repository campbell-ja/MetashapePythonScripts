# This script created by Joseph Aaron Campbell - 10/2020

""" Set up Working Environment """
# import Metashape library module
import Metashape
# create a reference to the current project via Document Class
doc = Metashape.app.document
# set reference for the currently active chunk
activeChunk = Metashape.app.document.chunk

# Estimate image quality
# this populates the 'Quality' column in the photos pane, under 'details' view
# this is not indicative of the actual image quality and is just here for example
activeChunk.analyzePhotos()