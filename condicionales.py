# _*_ coding: utf-8 _*_
#repaso de las estructuras de toma de decisiones
#dado un numero escribir el dia de la semana al que corresponde
dia= input('ingrese un numero del 1 al 7: ')
dia_seleccionado = ''
valido = True
#si el dia es el numero entonces decimos que es lunes
if dia== 1:
    dia_seleccionado = 'Lunes'
elif dia == 2:
    dia_seleccionado = 'Martes'
elif dia == 3:
    dia_seleccionado = 'Miercoles'
elif dia == 4:
    dia_seleccionado = 'Jueves'
elif dia == 5:
    dia_seleccionado = 'Viernes'
elif dia == 6:
    dia_seleccionado = 'Sabado'
elif dia == 7:
    dia_seleccionado = 'Domingo'
else:
    valido = False
    print "ingresa un numero valido del 1 al 7"
if valido == True:
    print "El numero " + str(dia) + " corresponde al dia " + dia_seleccionado