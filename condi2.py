# _*_ coding: utf-8 _*_
#solicitar una calificacion de un alumno entre el 0 y el 10
#vamos a imprimir si aprobo o reprobo
try:
    calificacion = int(input('ingrese una calificacion entre 0 y 10'))

    if calificacion >= 6 and calificacion <= 10 :
         print "aprobado 😍"
    elif calificacion >= 0 and calificacion <= 5 :
        print "reprobado 🤣"
    else:
        print "ingrese una calificacion entre 0 y 10 🤔 "
except Exception as error:
    print "Oh oh creo que ingresaste una letra 👀 , te estoy pidiendo numero"
    print "problema: " + error.message