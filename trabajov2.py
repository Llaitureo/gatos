#gatos
import csv

gatos =[]

with open('trabajo.csv','w') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['raza gato','peso en kg','color'])

while True:
    print('MENÚ DE GATOS')
    print('\nopc.1 = añadir razas de gatos.')
    print('opc.2 = ver razas de gatos.')
    print('opc.3 = salir.')
    while True:
        try:   
            opc = int(input('\nseleccióne una opción: '))
            if opc>0:
                break
        except:
            print('numero entero, sin n.0, porfavor.')

    if opc in (1,2,3):
        if opc == 1:
            print('AGREGAR RAZA GATO')
            while True:
                raza = input('\nintroduzca la raza del gato: ')
                if len(raza)>2 and raza.isalpha:
                    print('agregado con éxito.')
                    break
                else:
                    print('el nombre más corto es de 3 carácteres, tampoco debería poner numeros o símbolos.')
            while True:
                try:
                    peso = int(input('ingrese el peso promedio en kg de la raza: '))
                    if peso>0:
                        print('agregado con éxito.')
                        break
                except:
                    print('no decimales ni letras.')
            while True:
                color = input('ingrese el color que representa al gato: ')
                if len(color)>2 and color.isalpha:
                    print('agregado con éxito.')
                    break
                else:
                    print('no debería poner numeros o símbolos, tampoco más corto que 3 letras.')
            
            gatos =[raza, peso, color]
            with open('trabajo.csv', 'a+', newline="") as csvfile: 
                escritor = csv.writer(csvfile)  
                escritor.writerow(gatos)
        elif opc == 2:
            with open('trabajo.csv', 'r', newline="") as csvfile:
                lector = csv.reader(csvfile)
                for gatos in lector:
                    print(gatos)
        else:
            print('adios!')
            break
    else:
        print('opción incorrecta.')

#diosito, ayudameeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee.