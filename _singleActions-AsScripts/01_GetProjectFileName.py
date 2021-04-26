# This script created by Joseph Aaron Campbell - 10/2020

""" Set up Working Environment """
# import Metashape library module
import Metashape
# create a reference to the current project via Document Class
doc = Metashape.app.document
# set reference for the currently active chunk
activeChunk = Metashape.app.document.chunk

""" Get the Project File Name from User Input """
# prompt the user with the 'save as' gui and store the project file name
# returns the full path as is.
projectFileName = Metashape.app.getSaveFileName("Please input the Project File Name", "Metashape Project (*.psx)")
try:
    doc.save(projectFileName)
except RuntimeError:
    Metashape.app.messageBox("Can't save project")