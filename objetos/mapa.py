#importar la clase o el archivo estados para utilizar la clase llamda estados
from clases.estados import estados
import webbrowser

#crear nuestro primer estado
sinaloa = estados()
#asignar valor a los atributos del estado de sinaloa
sinaloa.clave = 25
sinaloa.nombre = "SINALOA"
sinaloa.poblacion = 3027000

#ejecutar la funcion con la que obtenes poblacion del estado
sinaloa.obtener_poblacion()

#creamos otro estado usando el costructor
durango = estados(34, 'DURANGO', 0, 0, 654876)
durango.obtener_poblacion()

#establecer ubicacion a sinaloa y durando, obteniendo el enlace de google maps
sinaloa.establecer_ubicacion('25.002778', '-107.502778')
url = sinaloa.obtener_enlace_google_maps()
print url
webbrowser.open(url)

durango.establecer_ubicacion('24.05718', '-104.53320')
webbrowser.open(durango.obtener_enlace_google_maps())
