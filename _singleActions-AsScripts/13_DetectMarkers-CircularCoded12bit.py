# This script created by Joseph Aaron Campbell - 10/2020

""" Set up Working Environment """
# import Metashape library module
import Metashape
# create a reference to the current project via Document Class
doc = Metashape.app.document
# set reference for the currently active chunk
activeChunk = Metashape.app.document.chunk

"""Detect Markers"""
# Detect Circular 12bit coded markers
# Coded target options: [CircularTarget12bit, CircularTarget14bit, CircularTarget16bit, CircularTarget20bit]
activeChunk.detectMarkers\
    (
        target_type=Metashape.TargetType.CircularTarget12bit,
        tolerance=25,
        filter_mask=False,
        inverted=False,
        noparity=False,
        maximum_residual=5,
        minimum_size=0,
        minimum_dist=5
    )