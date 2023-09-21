#definir la clase estados

class estados:
    #costructoror
    def __init__(self, clave =0, nombre='', lat=0, lon=0, poblacion=0):
        self.clave      =clave
        self.nombre     =nombre
        self.lat        =lat
        self.lon        =lon
        self.poblacion  =poblacion
    def  obtener_poblacion (self):
        print "la poblacion del estado " + self.nombre + " es de " + str(self.poblacion) + (" habitantes")
        return self.poblacion

    def establecer_ubicacion (self, latitud, longitud):
        self.lat = latitud
        self.lon = longitud
        print "se establecio la ubicacion del estado correctamente"


    def obtener_enlace_google_maps(self):
        enlace= "https://www.google.com/maps/@"+self.lat+","+self.lon+",8z?entry=ttu"
        return enlace