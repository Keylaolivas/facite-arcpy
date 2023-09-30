# _*_ coding: utf-8 _*_
import arcpy

import csv

arcpy.env.overwriteOutput = True

parada_autobuses =r"C:\Users\FOTO_03\PycharmProjects\facite-arcpy\RECURSOS\Data\SanFrancisco.gdb\Bus_Stops"
censo = r"C:\Users\FOTO_03\PycharmProjects\facite-arcpy\RECURSOS\Data\SanFrancisco.gdb\CensusBlocks2010"
seleccion_paradas= r"C:\Users\FOTO_03\PycharmProjects\facite-arcpy\RECURSOS\Data\SanFrancisco.gdb\Seleccion"
buffer =  r"C:\Users\FOTO_03\PycharmProjects\facite-arcpy\RECURSOS\Data\SanFrancisco.gdb\Buffer"
resultado =  r"C:\Users\FOTO_03\PycharmProjects\facite-arcpy\RECURSOS\Data\SanFrancisco.gdb\Interseccioncenso"


'''
arcpy.Select_analysis(parada_autobuses, seleccion_paradas, "NAME = '14 OB' AND BUS_SIGNAG = 'Lowell St.'")
print "seleccion finalizada"
arcpy.Buffer_analysis(seleccion_paradas, buffer, "100 Meters")
print "buffer finalizado"
arcpy.Intersect_analysis([censo, buffer], resultado)
print "Interseccion finalizada"
'''

interseccion_datos = { }
with arcpy.da.SearchCursor(resultado, ["POP10", "STOPID", "NAME"]) as cursor:
    for fila in cursor:
        stop_id = fila [1]
        pop10 = fila [0]
        name = fila [2]
        if stop_id not in interseccion_datos.keys():
        # sino existe en el diccionario lo agregamos
            interseccion_datos[stop_id] = [pop10]
        else:
            #si ya estaba gregado en el diccionario entoces spñp agregamos el pop10
            interseccion_datos[stop_id].append(pop10)

print "informacion del Diccionario"
print interseccion_datos