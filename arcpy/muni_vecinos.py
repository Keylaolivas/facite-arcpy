#_*_ coding: utf-8 _*_
import arcpy
import csv
arcpy.env.overwriteOutput = True
municipios = r'C:\Users\FOTO_03\PycharmProjects\facite-arcpy\muni2018\muni_2018cw.shp'
municipios_csv = r'C:\Users\FOTO_03\PycharmProjects\facite-arcpy\muni2018\municipios.csv'
arcpy.MakeFeatureLayer_management(municipios, "municipios_capa")
total_muni = arcpy.GetCount_management("municipios_capa")[0]
print total_muni
for i in range(0,  int(total_muni)):

    FID = "FID =" + str(i)
    seleccionado = arcpy.SelectLayerByAttribute_management("municipios_capa ", "NEW_SELECTION", FID)

    for columna in arcpy.da.SearchCursor(seleccionado, ["NOM_MUN", "NOM_ENT"]):
        NOMBRE_MUNICIPIO = columna[0].encode('utf-8')
        NOMBRE_ESTADO = columna[1].encode('utf-8')
        print ("{0} - Estado: {1} ---------- Minicipio: {2}".format(i, NOMBRE_ESTADO, NOMBRE_MUNICIPIO))