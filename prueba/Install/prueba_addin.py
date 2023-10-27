import functools
import threading

import arcpy
import pythonaddins
import webbrowser

class HerramientaClass3(object):
    """Implementation for herramienta_addin.tool (Tool)"""
    def __init__(self):
        self.enabled = True
        self.cursor = 3
        self.shape = "NONE" # Can set to "Line", "Circle" or "Rectangle" for interactive shape drawing and to activate the onLine/Polygon/Circle event sinks.
    def onMouseDown(self, x, y, button, shift):
        pass
    def onMouseDownMap(self, x, y, button, shift):
        try:
            coordenada_x = x
            coordenada_y = y
            #obtener una referencia a las capas de nuestro mapa en arcmap
            mapa_nxd = arcpy.mapping.MapDocument("CURRENT")
            #OBTENER LA REFERENCIA A LA VISTA DEL MAPA
            vista_mapa = mapa_nxd.activeView
            #generar una referencia espacial para la vista que se encuntra activa
            referencia_espacial = arcpy.mapping.ListDataFrames(mapa_nxd)[0].spatialReference
            #obtener el codigo de la referencia espacial
            #crear un punto para extraer las coordenadas en grados
            punto = arcpy.Point(coordenada_x, coordenada_y)
            #asignar una referencia espacial al punto
            punto_referenciado = arcpy.PointGeometry(punto, referencia_espacial)
            referencia_espacial_grados = arcpy.SpatialReference(4326)
            #extraer las coordenadas en grados del punto referenciado
            coordenadas = punto_referenciado.projectAs(referencia_espacial_grados)
            x_coord = float(coordenadas.firstPoint.X)
            y_coord = float(coordenadas.firstPoint.Y)
            url = "http://maps.google.com/?cbll={0},{1}&cbp=12,90,0,0,5&layer=c".format(y_coord, x_coord)
            def ejecutar_proceso(function):
                @functools.wraps(function)
                def fn(*args, **kwargs):
                    tarea = threading.Thread(target=function, args=args, kwargs=kwargs)
                    tarea.start()
                    tarea.join()
                return fn
            navegador = ejecutar_proceso(webbrowser.open)
            navegador( url, new=2)
            #pythonaddins.MessageBox("lat:" + str(coordenadas.firstPoint.X) + "lon:" + str(coordenadas.firstPoint.Y), "Coordenadas en grados")
            print (url)
            arcpy.AddMessage(url)
        except Exception as e:
            pythonaddins.MessageBox(e.message, "Error")

    def onMouseUp(self, x, y, button, shift):
        pass
    def onMouseUpMap(self, x, y, button, shift):
        pass
    def onMouseMove(self, x, y, button, shift):
        pass
    def onMouseMoveMap(self, x, y, button, shift):
        pass
    def onDblClick(self):
        pythonaddins.MessageBox("Hola", "Heramienta")
    def onKeyDown(self, keycode, shift):
        pass
    def onKeyUp(self, keycode, shift):
        pass
    def deactivate(self):
        pass
    def onCircle(self, circle_geometry):
        pass
    def onLine(self, line_geometry):
        pass
    def onRectangle(self, rectangle_geometry):
        pass

class saludarClass(object):
    """Implementation for saludar_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.MessageBox("Hola", "Saludo")
