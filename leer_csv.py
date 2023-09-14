# _*_ coding: utf-8 _*_

import csv

ubicacion_archivo = 'csv/data_estados.csv'
datos = {}
total_localidades = 0
with open(ubicacion_archivo, mode= 'r') as archivo:
    datos = csv.DictReader(archivo)

    for estado in datos:
        if estado['CVE_ENT'] == "25" and estado['CVE_MUN'] == '006':
            print estado['NOM_ENT'] + "-" + estado['NOM_MUN']+ "-" + estado['NOM_LOC'] + " coordenadas: (" + estado['LAT_DEC'] + "," + estado['LON_DEC'] + ")"
            total_localidades += 1

print "total de localidades del csv 🗺:" + str(total_localidades)
