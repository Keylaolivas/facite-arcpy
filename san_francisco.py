# _*_ coding: utf-8 _*_
import arcpy

import csv

arcpy.env.overwriteOutput = True

parada_autobuses =r"C:\Users\FOTO_03\PycharmProjects\facite-arcpy\Recursos\8662_ArcPyArcGIS_2\Data\SanFrancisco.gdb\Bus_Stops"
censo = r"C:\Users\FOTO_03\PycharmProjects\facite-arcpy\Recursos\8662_ArcPyArcGIS_2\Data\SanFrancisco.gdb\CensusBlocks2010"
seleccion_paradas= r"C:\Users\FOTO_03\PycharmProjects\facite-arcpy\Recursos\8662_ArcPyArcGIS_2\Data\SanFrancisco.gdb\Seleccion"
buffer =  r"C:\Users\FOTO_03\PycharmProjects\facite-arcpy\Recursos\8662_ArcPyArcGIS_2\Data\SanFrancisco.gdb\Buffer"
resultado =  r"C:\Users\FOTO_03\PycharmProjects\facite-arcpy\Recursos\8662_ArcPyArcGIS_2\Data\SanFrancisco.gdb\Interseccioncenso"



arcpy.Select_analysis(parada_autobuses, seleccion_paradas, "NAME = '14 OB' AND BUS_SIGNAG = 'Lowell St.'")
print "seleccion finalizada"
arcpy.Buffer_analysis(seleccion_paradas, buffer, "100 Meters")
print "buffer finalizado"
arcpy.Intersect_analysis([censo, buffer], resultado)
print "Interseccion finalizada"
