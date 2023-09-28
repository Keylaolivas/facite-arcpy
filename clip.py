# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# clip.py
# Created on: 2023-09-21 16:54:45.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
sinaloa_shp = "C:\\sig\\SIG_1\\sinaloa.shp"
dibujo_shp = "C:\\sig\\SIG_1\\dibujo.shp"
sinaloa_clip_shp = "C:\\sig\\SIG_1\\sinaloa_clip.shp"

# Process: Clip
arcpy.Clip_analysis(sinaloa_shp, dibujo_shp, sinaloa_clip_shp, "")
