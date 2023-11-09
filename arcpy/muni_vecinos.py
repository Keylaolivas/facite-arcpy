#_*_ coding: utf-8 _*_
import arcpy
import csv
arcpy.env.overwriteOutput = True
municipios = r'C:\Users\FOTO_03\PycharmProjects\facite-arcpy\muni2018\muni_2018cw.shp'
municipios_csv = r'C:\Users\FOTO_03\PycharmProjects\facite-arcpy\muni2018\municipios.csv'
arcpy.MakeFeatureLayer_management(municipios, "municipios_capa")
total_muni = arcpy.GetCount_management("municipios_capa")[0]
lista_excel = []
print total_muni
for i in range(0,  int(5)):

    FID = "FID =" + str(i)
    seleccionado = arcpy.SelectLayerByAttribute_management("municipios_capa ", "NEW_SELECTION", FID)

    for columna in arcpy.da.SearchCursor(seleccionado, ["NOM_MUN", "NOM_ENT"]):
        NOMBRE_MUNICIPIO_seleccionado = columna[0].encode('utf-8')
        NOMBRE_ESTADO = columna[1].encode('utf-8')
        print ("{0} - Estado: {1} ---------- Minicipio: {2}".format(i, NOMBRE_ESTADO, NOMBRE_MUNICIPIO_seleccionado))
        #crear una capa temporal de municipios
        muni_vecinos_capa = arcpy.SelectLayerByLocation_management("municipios_capa", "INTERSECT", seleccionado)
        for vecino in muni_vecinos_capa:
            for columna in arcpy.da.SearchCursor(vecino, ["FID", "NOM_MUN", "NOM_ENT"]):
                NOMBRE_MUNICIPIO = columna[1].encode('utf-8')
                NOMBRE_ESTADO = columna[2].encode('utf-8')
                print ("vecino {0} - Estado: {1} ---------- Minicipio: {2}".format(i, NOMBRE_ESTADO, NOMBRE_MUNICIPIO_seleccionado))
                fila = list(columna)
                fila.append(NOMBRE_MUNICIPIO_seleccionado)
                lista_excel.append((fila))
with open (municipios_csv, "wb") as archivo:
    csvwriter= csv.writer (archivo, delimiter=",")
    cabecera  = ["FID", "NOM_MUN", "NOM_ENT", "MUN_SELECCIONADO"]
    csvwriter.writerow(cabecera)
    for fila in lista_excel:
        csvwriter.writerow(fila)
        print "proceso finalizado"

