menu = [[1,'Suma'],[2,'Resta'],[3,'Multiplicación'],[4,'División'],[0,'terminar']]
salir = False

print ('Ingrese los números que desea operar: ')
num1 = int(input('Primer número: '))
num2 = int(input('Segundo número: '))
while (salir == False):
    for i in range (len(menu)):
        print (str(menu[i][0]) + ') ' + menu[i][1])
    accion = int(input('¿Qué acción desea realizar?: '))
#deriva a los modulos correspondientes
    if accion == 1:
        print ('La suma es ' + str(num1 + num2))
    elif accion == 2:
        print ('La resta es: '+str(num1 - num2))
    elif accion == 3:
        print ('La multiplicación es: '+str(num1 * num2))
    elif accion == 4:
        print ('La división es: '+str(num1 / num2))
    else:
        print ('Gracias por utilizar el servicio.')
        salir = True