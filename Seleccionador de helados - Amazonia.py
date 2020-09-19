'''
Programa para elegir gustos de helados de Amazonia

Pendiente 
- loopear todo con un While True
- poner un validador de input
- definir acciones para cada menú y submenú
'''

# Importando RANDOM, después ver si importo solo alguna función específica
import random

# Gustos
Crema = ['Banana Split', 'Mascarpone con frutos rojos', 'Vainilla', 'Bombon rocher', 'Crema Americana', 'Sambayón', 'Samb. c/frutillas', 'Samb. c/almendras', 'Frutilla a la crema', 'Tiramisú', 'Granizado']
Agua = ['Limón', 'Frutilla', 'Melón', 'Durazno', 'Naranja', 'Maracuyá', 'Mouse limón granizado', 'Mandarina']
DulceDeLeche = ['Dulce de Leche', 'D.L. granizado', 'D.L. con brownie', 'D.L. doble', 'D.L. con nueces']
Chocolate = ['Chocolate', 'Choco donna', 'Choco suizo', 'Choco italiano', 'Choco con almendras']
Gustos_Totales = (Crema + Agua + DulceDeLeche + Chocolate)

# Precios
Pesos = {'1/4kg' : 150, '1,2kg' : 250, '1kg' : 450}



#Saludo
print('\nHola! Bienvenido al programa para elegir tus gustos de helado de Amazonia\n')

# Menu principal
def menu_principal():
    print('Menu principal:')
    print('1. Ver menú por categoría')
    print('2. Ver precios')
    print('3. Ruleta de gustos\n')
    print('4. Salir')
    accion = input('Elegí el número de la opción que querés: ')
    while accion not in ['1','2','3','4']: 
        print('\nNo elegiste una opción válida.\nElegí un número del 1 al 3.\n')
        print('Menu principal:')
        print('1. Ver menú por categoría')
        print('2. Ver precios')
        print('3. Ruleta de gustos\n')
        print('4. Salir')
        accion = input('Elegí el número de la opción que querés: ')
    if accion == '1':
        menu_categorias()
    elif accion == '2':
        menu_precios()
    elif accion == '3':
        menu_random()
    elif accion == '4':
        print('Hasta luego!!!')

# Opción 1: Submenu de categorías
def menu_categorias():
    print('Las categorías de helados son:')
    print('1. Crema \n2. Agua \n3. Dulce de Leche \n4. Chocolate')
    print('9. Volver al Menú Principal.')
    categoria = input('Elegí el número de la opción deseadad: ')
    while categoria not in ['1','2','3','4','9']:
        print('\nNo elegiste una opción válida.\nElegí un número del 1 al 4 o 9 para volver al menú principal.\n')
        print('Las categorías de helados son:')
        print('1. Crema \n2. Agua \n3.Dulce de Leche \n4.Chocolate')
        print('\n9. Volver al Menú Principal.')
        categoria = input('Elegí el número de la opción deseadad: ')
    if categoria == '1':
        print('Los gustos de Crema son:')
        ci = 1
        for c in Crema:
            print(str(ci)+". "+str(c))
            ci += 1
        acc_categoría = input('\nSeleccioná la opción deseada:\n1. Para Menú de Categoría.\n2. Para Menú Principal\n.')
        while acc_categoría not in ['1','2']:
            print('Opción no válida')
            acc_categoría = input('\n1. Menú de Categoría.\n2. Menú Principal')
        if acc_categoría == '1':
            menu_categorias()
        elif acc_categoría == '2':
            menu_principal()
    elif categoria == '2':
        print('Los gustos de Agua son:')
        ci = 1
        for a in Agua:
            print(str(ci)+". "+str(a))
            ci += 1
        acc_categoría = input('\nSeleccioná la opción deseada:\n1. Para Menú de Categoría.\n2. Para Menú Principal\n.')
        while acc_categoría not in ['1','2']:
            print('Opción no válida')
            acc_categoría = input('\n1. Menú de Categoría.\n2. Menú Principal')
        if acc_categoría == '1':
            menu_categorias()
        elif acc_categoría == '2':
            menu_principal()
    elif categoria == '3':
        print('Los gustos de Dulce de Leche son:')
        ci = 1
        for d in DulceDeLeche:
            print(str(ci)+". "+str(d))
            ci += 1
        acc_categoría = input('\nSeleccioná la opción deseada:\n1. Para Menú de Categoría.\n2. Para Menú Principal\n.')
        while acc_categoría not in ['1','2']:
            print('Opción no válida')
            acc_categoría = input('\n1. Menú de Categoría.\n2. Menú Principal')
        if acc_categoría == '1':
            menu_categorias()
        elif acc_categoría == '2':
            menu_principal()
    elif categoria == '4':
        print('Los gustos de Chocolate son:')
        ci = 1
        for ch in Chocolate:
            print(str(ci)+". "+str(ch))
            ci += 1
        acc_categoría = input('\nSeleccioná la opción deseada:\n1. Para Menú de Categoría.\n2. Para Menú Principal\n.')
        while acc_categoría not in ['1','2']:
            print('Opción no válida')
            acc_categoría = input('\n1. Menú de Categoría.\n2. Menú Principal')
        if acc_categoría == '1':
            menu_categorias()
        elif acc_categoría == '2':
            menu_principal()
    elif categoria == '9':
        menu_principal()


# Opción 2: Submenu de precios
def menu_precios():
    print("Los precios son:")
    for key,val in Pesos.items():
        print(str(key)+": "+str(val))
    acc_precio = input('\nPara volver al Menú Principal presioná 1: ')
    while acc_precio != '1':
        print('Opción no válida')
        acc_precio = input('\nPara volver al Menú Principal presioná 1: ')
    if acc_precio == '1':
        menu_principal()


# Opción 3: Submenu de random
def menu_random():
    # Configuración de Random 1
    def menu_random_1():
        print('Elegiste la opción: Random entre todos los gustos')
        cantidad_gustos = int(input('¿Cuantos gustos queres elegir?: \nMáximo 3 gustos: '))
        while cantidad_gustos not in [1,2,3]:
            print('Opción no valida!\nSolo podes elegir entre 1 y 3 gustos.')
            cantidad_gustos = int(input('¿Cuantos gustos queres elegir?: \nMáximo 3 gustos: '))  
        print('\nTus gustos elegidos son: ')
        print(random.sample(Gustos_Totales, k=cantidad_gustos))
        acc_random = input('\nSeleccioná la opción deseada:\n1. Menú de Random.\n9. Menú Principal.\n.')
        while acc_random not in ['1','2','9']:
            print('Opción no válida')
            acc_random = input('\n1. Menú de Random.\n9. Menú Principal.\n.')
        if acc_random == '1':
            menu_random()
        elif acc_random == '9':
            menu_principal()

    #Configuración de Random 2
    def menu_random_2():
        lista_gustos_SiNo = []
        lista_gustos = []
        
        print('Elegiste la opción: Un gusto de cada categoría que elijas')
        Crema_SiNo = input('¿Querés un helado de Crema? S/N: ').lower()
        while Crema_SiNo not in ['s','n']:
            print('Opción no válida!\n Ingresá "S" o "N": ')
            Crema_SiNo = input('¿Querés un helado de Crema? S/N: ').lower()
        if Crema_SiNo == 's':
            lista_gustos_SiNo.append(1)
        elif Crema_SiNo == 'n':
            lista_gustos_SiNo.append(0)
        Agua_SiNo = input('¿Querés un helado de Agua? S/N: ').lower()
        while Agua_SiNo not in ['s','n']:
            print('Opción no válida!\n Ingresá "S" o "N": ')
            Agua_SiNo = input('¿Querés un helado de Agua? S/N: ').lower()
        if Agua_SiNo == 's':
            lista_gustos_SiNo.append(1)
        elif Agua_SiNo == 'n':
            lista_gustos_SiNo.append(0)
        DulcedeLeche_SiNo = input('¿Querés un helado de Dulce de Leche? S/N: ').lower()
        while DulcedeLeche_SiNo not in ['s','n']:
            print('Opción no válida!\n Ingresá "S" o "N": ')
            DulcedeLeche_SiNo = input('¿Querés un helado de Dulce de Leche? S/N: ').lower()
        if DulcedeLeche_SiNo == 's':
            lista_gustos_SiNo.append(1)
        elif DulcedeLeche_SiNo == 'n':
            lista_gustos_SiNo.append(0)
        Chocolate_SiNo = input('¿Querés un helado de Chocolate? S/N: ').lower()
        while Chocolate_SiNo not in ['s','n']:
            print('Opción no válida!\n Ingresá "S" o "N": ')
            Chocolate_SiNo = input('¿Querés un helado de Chocolate? S/N: ').lower()
        if Chocolate_SiNo == 's':
            lista_gustos_SiNo.append(1)
        elif Chocolate_SiNo == 'n':
            lista_gustos_SiNo.append(0)
        
        print(lista_gustos_SiNo)

        #Creando lista de gustos elegidos
        if lista_gustos_SiNo[0] == 1:
            print('Crema')
            lista_gustos.append(random.choice(Crema))
        if lista_gustos_SiNo[1] == 1:
            print('Agua')
            lista_gustos.append(random.choice(Agua))
        if lista_gustos_SiNo[2] == 1:
            print('DDL')
            lista_gustos.append(random.choice(DulceDeLeche))
        if lista_gustos_SiNo[3] == 1:
            print('Chocolate')
            lista_gustos.append(random.choice(Chocolate))
        
        #Mostrando lista de gustos
        print('\nTus gustos seleccionados son:')
        xi = 1
        for i in lista_gustos:
            print(str(xi)+". "+i)
            xi += 1
        acc_random = input('\nSeleccioná la opción deseada:\n1. Menú de Random.\n9. Menú Principal.\n.')
        while acc_random not in ['1','2','9']:
            print('Opción no válida')
            acc_random = input('\n1. Menú de Random.\n9. Menú Principal.\n.')
        if acc_random == '1':
            menu_random()
        elif acc_random == '9':
            menu_principal()        


    #Acción de Random una vez configuradas las opciones
    acc_random = input('Podés elegir:\n1. Random entre todos los gustos.\n2. Un gusto de cada categoría que elijas.\n9. Volver al menú principal.\n:')
    while acc_random not in ['1','2','9']:
        print('Opción no válida!\nElegí entre las opciones 1, 2 y 9')
        acc_random = input('Podés elegir:\n1. Random entre todos los gustos.\n2. Un gusto de cada categoría que elijas.\n9. Volver al menú principal.\n:')
    if acc_random == '1':
        menu_random_1()
    elif acc_random == '2':
        menu_random_2()
    elif acc_random == '9':
        menu_principal()


menu_principal()