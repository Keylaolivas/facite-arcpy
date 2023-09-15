# _*_ coding: utf-8 _*_

#como declarar una funcion  (funcion que nos saludes)
def saludar(): #funcion que no recibe ningun parametro
    print "Hola te saludo"

def pendiente():  #funcion que no hace nada
    pass          #sirve para que nuestra funcion no nos detecte error
def adivinar_edad(dia, mes, anio):
    #empezar a caulcular la edad
    actual = 2023
    mes_actual = 9
    edad= actual - anio
    #si el mes es mayor al mes actual entonces restamos uno a la edad
    if mes > mes_actual:
        edad = edad -1

    print "la edad es ; " + str(edad)


#crear una funcion que reciba parametros opcionales
def definnir_sexualidad(genero= "No binario"):
    print "Elegiste ser : " + genero


#ejecutar la funcion saludar
saludar()
adivinar_edad(27, 10,2003)

definnir_sexualidad("Masculino")
definnir_sexualidad("Femenino")
definnir_sexualidad()