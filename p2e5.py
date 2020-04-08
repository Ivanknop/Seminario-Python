'''
Generar un menú que te permita realizar las siguientes opciones:
Menú de opciones para la lista de números a ingresar:
1: ingresar números
2: ordenar números
3: calcular el máximo
4: calcular el mínimo
5: calcular el promedio
0: para terminar
Se debe repetir hasta que se ingrese la opción 0. Se debe permitir agregar números aún luego de
haber utilizado las demás operaciones utilizando la opción 1. En caso que no se haya ingresado
ningún número indicar que la lista está vacía. Investigue las funciones max, min y sum.
'''
lista = []
#Crea menú
menu = [[1,'ingresar números'],[2,'ordenar números'],[3,'calcular máximo'],[4,'calcular el mínimo'],[5,'calcular el promedio'],[0,'terminar']]

def ingresar():
    l=[]
    num = int(input('Ingrese un numero (-9999 para terminar):'))
    while (num != -9999) :
        l.append(num)
        num = int(input('Ingrese otro número (-9999 para terminar):'))
    return l

def ordenar (lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista [j] > lista [j+1]:
                lista[j],lista[j+1] = lista [j+1],lista[j]
    return (lista)

def promedio (lista):
    prom = 0
    for i in range(len(lista)):
        prom = prom + lista [i]
    prom = prom / len(lista)    
    return prom
salir = False 


while (salir == False):
    for i in range (len(menu)):
        print (str(menu[i][0]) + ') ' + menu[i][1])
    accion = int(input('¿Qué acción desea realizar?: '))
#deriva a los modulos correspondientes
    if accion == 1:
        #print ('Usted eligio ' + menu[accion-1][1])
        lista = lista + ingresar()
        print (lista)
    elif accion == 2:
        lista2 = ordenar (lista)
        print (lista2)
        #print ('Usted eligio ' + menu[accion-1][1])
    elif accion == 3:
        print ('El número máximo es: ' + str(max(lista)))
        print ('Usted eligio ' + menu[accion-1][1])
    elif accion == 4:
        print ('El número mínimo es: ' + str(min(lista)))
        #print ('Usted eligio ' + menu[accion-1][1])
    elif accion == 5:
        prom = promedio(lista)
        print ('El promedio de los numeros cargados es: ' + str(prom))
    else:
        print ('Gracias por utilizar el servicio.')
        salir = True

