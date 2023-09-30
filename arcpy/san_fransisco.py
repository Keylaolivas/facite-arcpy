#_*_ coding: utf-8 _*_
import arcpy   #libreria de arcgis
import csv      #libreria para generar CSV


#permitir sobreescribir los archivos existentes
arcpy.env.overwriteOutput = True

#archivo de entrada
parada_autobuses = r"C:\Users\FOTO_06\PycharmProjects\facite-arcpy\RECURSOS\Data\SanFrancisco.gdb\Bus_Stops"
censo = r"C:\Users\FOTO_06\PycharmProjects\facite-arcpy\RECURSOS\Data\SanFrancisco.gdb\CensusBlocks2010"
seleccion_paradas = r"C:\Users\FOTO_06\PycharmProjects\facite-arcpy\RECURSOS\Data\SanFrancisco.gdb\seleccion"

#archivos generados
interseccion = r"C:\Users\FOTO_06\PycharmProjects\facite-arcpy\RECURSOS\Data\SanFrancisco.gdb\InterseccionesCenso"
buffer = r"C:\Users\FOTO_06\PycharmProjects\facite-arcpy\RECURSOS\Data\SanFrancisco.gdb\Buffer"

'''
#seleccionar Bus stops que coincidan con el name 14 OB y el bus_signan Lowell st.
arcpy.Select_analysis(parada_autobuses, seleccion_paradas,  "NAME = '14 OB' AND BUS_SIGNAG = 'Lowell St.'")
print "Seleccion Finalizada (●'◡'●)"
#HACER BUFFER DE 100 MTRS
arcpy.Buffer_analysis(seleccion_paradas, buffer,  "100 Meters")
print "Buffer Finalizado ^_^"
# hacer interseccion de census block con el buffer
arcpy.Intersect_analysis([censo, buffer], interseccion )
print "Interseccion Finalizada ಥ_ಥ"
'''
#