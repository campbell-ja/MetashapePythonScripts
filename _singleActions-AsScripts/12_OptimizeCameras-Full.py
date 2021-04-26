# This script created by Joseph Aaron Campbell - 10/2020

""" Set up Working Environment """
# import Metashape library module
import Metashape
# create a reference to the current project via Document Class
doc = Metashape.app.document
# set reference for the currently active chunk
activeChunk = Metashape.app.document.chunk

""" Optimize Cameras with Basic Fittings"""
activeChunk.optimizeCameras \
    (
        fit_f=True,
        fit_cx=True,
        fit_cy=True,
        fit_b1=True,
        fit_b2=True,
        fit_k1=True,
        fit_k2=True,
        fit_k3=True,
        fit_k4=False,
        fit_p1=True,
        fit_p2=True,
        fit_corrections=False,
        adaptive_fitting=False,
        tiepoint_covariance=False
    )