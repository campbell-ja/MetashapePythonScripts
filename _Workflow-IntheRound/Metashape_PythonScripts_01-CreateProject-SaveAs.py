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

# prompt the user with the 'save as' gui and store the project file name
# returns the full path as is.
projectFileName = Metashape.app.getSaveFileName("Please input the Project File Name", "Metashape Project (*.psx)")
try:
    doc.save(projectFileName)
except RuntimeError:
    Metashape.app.messageBox("Can't save project")


""" Save the Project """
# save document assuming the file has already been saved at least once.
# if the document has NOT been saved previously..
# then provide the path between the ().
doc.save()