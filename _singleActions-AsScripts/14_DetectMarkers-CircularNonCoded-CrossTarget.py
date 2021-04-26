# This script created by Joseph Aaron Campbell - 10/2020

""" Set up Working Environment """
# import Metashape library module
import Metashape
# create a reference to the current project via Document Class
doc = Metashape.app.document
# set reference for the currently active chunk
activeChunk = Metashape.app.document.chunk

"""Detect Markers"""
# Detect Cross non-coded markers
# Non-coded target options: [CircularTarget, CrossTarget]
activeChunk.detectMarkers\
    (
        target_type=Metashape.TargetType.CrossTarget,
        tolerance=25,
        filter_mask=False,
        inverted=False,
        noparity=False,
        maximum_residual=5,
        minimum_size=0,
        minimum_dist=5
    )