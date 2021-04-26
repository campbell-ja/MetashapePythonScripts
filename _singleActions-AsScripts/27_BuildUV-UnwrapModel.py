# This script created by Joseph Aaron Campbell - 10/2020

""" Set up Working Environment """
# import Metashape library module
import Metashape
# create a reference to the current project via Document Class
doc = Metashape.app.document
# set reference for the currently active chunk
activeChunk = Metashape.app.document.chunk

"""Unwrap selected model"""
activeChunk.buildUV \
        (
        mapping_mode=Metashape.GenericMapping,
        page_count=1,
        adaptive_resolution=False
    )