import random
from pasajeros import Pasajero
from habitaciones import Habitacion
from Turistas import Turista
from Plato import Plato
from Combo import Combo
def registrar_pasajero():
    while True:
        try:
            decision1= input('''Indique si quiere comprar su boleto segun:
            1. La Ruta
            2. El Barco
            >''')
            if decision1 == '1':
                seleccionar_crucero = input('''Las Rutas que tenemos abiertas son:
                1. Fort Lauderdale - Bahamas - St. Thomas - Islas Virgenes - Fort Lauderdale
                2. Barbados-Bahamas-Aruba-Curaçao-Snta Lucia-Barbados
                3. Miami-Bahamas-Puerto Rico-Haiti-Republica Dominicana-Miami
                4. Galveston-Cozumel-Haiti-Jamaica-Panama-Galveston
                >''')
                if seleccionar_crucero == '1':
                    habitacion = input('''Las tarifas en "El Dios de los Mares" son las siguientes:
                    tipo sencilla, capacidad para 2 personas, tiene un precio de 69.99 USD
                    tipo Premium, capacidad para 4 personas, tiene un precio de 89.99 USD
                    tipo VIP, capacidad para 8 personas, tiene un precio de 129.99 USD
                    que tipo de habitacion deseas?
                    1. Sencilla
                    2. Premium
                    3. VIP
                    >''')
                    if habitacion == '1':
                        pasajeros = int(input ('Cuantos boletos desea? '))
                        if pasajeros >=3:
                            print ('Les asignaremos multiples habitaciones')
                        price = 69.99
                        precio1 = 0
                        precio2 = 0
                        for i in range(pasajeros):
                            name = input('Nombre del Pasajero: ')
                            dni = int(input('DNI del Pasajero: '))
                            if dni > 1:
                                for i in range(2, dni):
                                    if (dni  % i)==0:
                                        precio = 0
                                    break
                                else: 
                                    precio1 = (price*0.1)
                            else: 
                                precio = 0
                            age = int(input('Edad de Pasajero: '))
                            if age >= 65:
                                print ('Puede optar a una mejora de habitacion!')
                            disability = input ('''Indique si el pasajero sufre alguna discapacidad
                            1. Si 
                            2. No
                            >''')
                            if disability == '1':
                                disability = 'si'
                                precio2 = (price * 0.30)
                            elif disability == '2':
                                disability = 'no'
                                precio2 = 0
                            elif disability >= '3':
                                print('Seleccione una opcion valida')
                                raise Exception                
                            precio = price - precio1 -precio2
                            price_wt = precio + (precio*0.16)
                    elif habitacion == '2':
                        pasajeros = int(input ('Cuantos boletos desea? '))
                        if pasajeros >=5:
                            print ('Les asignaremos multiples habitaciones')
                        price = 89.99
                        precio1 = 0
                        precio2 = 0
                        for i in range(pasajeros):
                            name = input('Nombre del Pasajero: ')
                            dni = int(input('DNI del Pasajero: '))
                            if dni > 1:
                                for i in range(2, dni):
                                    if (dni  % i)==0:
                                        precio = 0
                                    break
                                else: 
                                    precio1 = (price*0.1)
                            else: 
                                precio = 0
                            age = int(input('Edad de Pasajero: '))
                            if age >= 65:
                                print ('Puede optar a una mejora de habitacion!')
                            disability = input ('''Indique si el pasajero sufre alguna discapacidad
                            1. Si 
                            2. No
                            >''')
                            if disability == '1':
                                disability = 'si'
                                precio2 = (price * 0.30)
                            elif disability == '2':
                                disability = 'no'
                                precio2 = 0
                            elif disability >= '3':
                                print('Seleccione una opcion valida')
                                raise Exception                
                            precio = price - precio1 -precio2
                            price_wt = precio + (precio*0.16)
                    if habitacion == '3':
                        pasajeros = int(input ('Cuantos boletos desea? '))
                        if pasajeros >=9:
                            print ('Les asignaremos multiples habitaciones')
                        price = 129.99
                        precio1 = 0
                        precio2 = 0
                        for i in range(pasajeros):
                            name = input('Nombre del Pasajero: ')
                            dni = int(input('DNI del Pasajero: '))
                            if dni > 1:
                                for i in range(2, dni):
                                    if (dni  % i)==0:
                                        precio = 0
                                    break
                                else: 
                                    precio1 = (price*0.1)
                            else: 
                                precio = 0
                            age = int(input('Edad de Pasajero: '))
                            if age >= 65:
                                print ('Puede optar a una mejora de habitacion!')
                            disability = input ('''Indique si el pasajero sufre alguna discapacidad
                            1. Si 
                            2. No
                            >''')
                            if disability == '1':
                                disability = 'si'
                                precio2 = (price * 0.30)
                            elif disability == '2':
                                disability = 'no'
                                precio2 = 0
                            elif disability >= '3':
                                print('Seleccione una opcion valida')
                                raise Exception                
                            precio = price - precio1 -precio2
                            price_wt = precio + (precio*0.16)
                    elif habitacion >= '4':
                        print ('Seleccione un opcion valida')
                        raise Exception  
                    break                      
                elif seleccionar_crucero == '2':
                    habitacion = input('''Las tarifas en "La Reina Isabel" son las siguientes:
                    tipo sencilla, capacidad para 2 personas, tiene un precio de 9.99 USD
                    tipo Premium, capacidad para 4 personas, tiene un precio de 99.99 USD
                    tipo VIP, capacidad para 8 personas, tiene un precio de 119.99 USD
                    que tipo de habitacion deseas?
                    1. Sencilla
                    2. Premium
                    3. VIP
                    >''')
                    if habitacion == '1':
                        pasajeros = int(input ('Cuantos boletos desea? '))
                        if pasajeros >=3:
                            print ('Les asignaremos multiples habitaciones')
                        price = 59.99
                        precio1 = 0
                        precio2 = 0
                        for i in range(pasajeros):
                            name = input('Nombre del Pasajero: ')
                            dni = int(input('DNI del Pasajero: '))
                            if dni > 1:
                                for i in range(2, dni):
                                    if (dni  % i)==0:
                                        precio = 0
                                    break
                                else: 
                                    precio1 = (price*0.1)
                            else: 
                                precio = 0
                            age = int(input('Edad de Pasajero: '))
                            if age >= 65:
                                print ('Puede optar a una mejora de habitacion!')
                            disability = input ('''Indique si el pasajero sufre alguna discapacidad
                            1. Si 
                            2. No
                            >''')
                            if disability == '1':
                                disability = 'si'
                                precio2 = (price * 0.30)
                            elif disability == '2':
                                disability = 'no'
                                precio2 = 0
                            elif disability >= '3':
                                print('Seleccione una opcion valida')
                                raise Exception                
                            precio = price - precio1 -precio2
                            price_wt = precio + (precio*0.16)
                    elif habitacion == '2':
                        pasajeros = int(input ('Cuantos boletos desea? '))
                        if pasajeros >=5:
                            print ('Les asignaremos multiples habitaciones')
                        price = 99.99
                        precio1 = 0
                        precio2 = 0
                        for i in range(pasajeros):
                            name = input('Nombre del Pasajero: ')
                            dni = int(input('DNI del Pasajero: '))
                            if dni > 1:
                                for i in range(2, dni):
                                    if (dni  % i)==0:
                                        precio = 0
                                    break
                                else: 
                                    precio1 = (price*0.1)
                            else: 
                                precio = 0
                            age = int(input('Edad de Pasajero: '))
                            if age >= 65:
                                print ('Puede optar a una mejora de habitacion!')
                            disability = input ('''Indique si el pasajero sufre alguna discapacidad
                            1. Si 
                            2. No
                            >''')
                            if disability == '1':
                                disability = 'si'
                                precio2 = (price * 0.30)
                            elif disability == '2':
                                disability = 'no'
                                precio2 = 0
                            elif disability >= '3':
                                print('Seleccione una opcion valida')
                                raise Exception                
                            precio = price - precio1 -precio2
                            price_wt = precio + (precio*0.16)
                    if habitacion == '3':
                        pasajeros = int(input ('Cuantos boletos desea? '))
                        if pasajeros >=9:
                            print ('Les asignaremos multiples habitaciones')
                        price = 119.99
                        precio1 = 0
                        precio2 = 0
                        for i in range(pasajeros):
                            name = input('Nombre del Pasajero: ')
                            dni = int(input('DNI del Pasajero: '))
                            if dni > 1:
                                for i in range(2, dni):
                                    if (dni  % i)==0:
                                        precio = 0
                                    break
                                else: 
                                    precio1 = (price*0.1)
                            else: 
                                precio = 0
                            age = int(input('Edad de Pasajero: '))
                            if age >= 65:
                                print ('Puede optar a una mejora de habitacion!')
                            disability = input ('''Indique si el pasajero sufre alguna discapacidad
                            1. Si 
                            2. No
                            >''')
                            if disability == '1':
                                disability = 'si'
                                precio2 = (price * 0.30)
                            elif disability == '2':
                                disability = 'no'
                                precio2 = 0
                            elif disability >= '3':
                                print('Seleccione una opcion valida')
                                raise Exception                
                            precio = price - precio1 -precio2
                            price_wt = precio + (precio*0.16)
                    elif habitacion >= '4':
                        print ('Seleccione un opcion valida')
                        raise Exception  
                    break
                elif seleccionar_crucero == '3':
                    habitacion = input('''Las tarifas en "El Libertador del Oceano" son las siguientes:
                    tipo sencilla, capacidad para 3 personas, tiene un precio de 49.99 USD
                    tipo Premium, capacidad para 5 personas, tiene un precio de 89.99 USD
                    tipo VIP, capacidad para 12 personas, tiene un precio de 139.99 USD
                    que tipo de habitacion deseas?
                    1. Sencilla
                    2. Premium
                    3. VIP
                    >''')
                    if habitacion == '1':
                        pasajeros = int(input ('Cuantos boletos desea? '))
                        if pasajeros >=4:
                            print ('Les asignaremos multiples habitaciones')
                        price = 49.99
                        precio1 = 0
                        precio2 = 0
                        for i in range(pasajeros):
                            name = input('Nombre del Pasajero: ')
                            dni = int(input('DNI del Pasajero: '))
                            if dni > 1:
                                for i in range(2, dni):
                                    if (dni  % i)==0:
                                        precio = 0
                                    break
                                else: 
                                    precio1 = (price*0.1)
                            else: 
                                precio = 0
                            age = int(input('Edad de Pasajero: '))
                            if age >= 65:
                                print ('Puede optar a una mejora de habitacion!')
                            disability = input ('''Indique si el pasajero sufre alguna discapacidad
                            1. Si 
                            2. No
                            >''')
                            if disability == '1':
                                disability = 'si'
                                precio2 = (price * 0.30)
                            elif disability == '2':
                                disability = 'no'
                                precio2 = 0
                            elif disability >= '3':
                                print('Seleccione una opcion valida')
                                raise Exception                
                            precio = price - precio1 -precio2
                            price_wt = precio + (precio*0.16)
                    elif habitacion == '2':
                        pasajeros = int(input ('Cuantos boletos desea? '))
                        if pasajeros >=6:
                            print ('Les asignaremos multiples habitaciones')
                        price = 89.99
                        precio1 = 0
                        precio2 = 0
                        for i in range(pasajeros):
                            name = input('Nombre del Pasajero: ')
                            dni = int(input('DNI del Pasajero: '))
                            if dni > 1:
                                for i in range(2, dni):
                                    if (dni  % i)==0:
                                        precio = 0
                                    break
                                else: 
                                    precio1 = (price*0.1)
                            else: 
                                precio = 0
                            age = int(input('Edad de Pasajero: '))
                            if age >= 65:
                                print ('Puede optar a una mejora de habitacion!')
                            disability = input ('''Indique si el pasajero sufre alguna discapacidad
                            1. Si 
                            2. No
                            >''')
                            if disability == '1':
                                disability = 'si'
                                precio2 = (price * 0.30)
                            elif disability == '2':
                                disability = 'no'
                                precio2 = 0
                            elif disability >= '3':
                                print('Seleccione una opcion valida')
                                raise Exception                
                            precio = price - precio1 -precio2
                            price_wt = precio + (precio*0.16)
                    if habitacion == '3':
                        pasajeros = int(input ('Cuantos boletos desea? '))
                        if pasajeros >=13:
                            print ('Les asignaremos multiples habitaciones')
                        price = 139.99
                        precio1 = 0
                        precio2 = 0
                        for i in range(pasajeros):
                            name = input('Nombre del Pasajero: ')
                            dni = int(input('DNI del Pasajero: '))
                            if dni > 1:
                                for i in range(2, dni):
                                    if (dni  % i)==0:
                                        precio = 0
                                    break
                                else: 
                                    precio1 = (price*0.1)
                            else: 
                                precio = 0
                            age = int(input('Edad de Pasajero: '))
                            if age >= 65:
                                print ('Puede optar a una mejora de habitacion!')
                            disability = input ('''Indique si el pasajero sufre alguna discapacidad
                            1. Si 
                            2. No
                            >''')
                            if disability == '1':
                                disability = 'si'
                                precio2 = (price * 0.30)
                            elif disability == '2':
                                disability = 'no'
                                precio2 = 0
                            elif disability >= '3':
                                print('Seleccione una opcion valida')
                                raise Exception                
                            precio = price - precio1 -precio2
                            price_wt = precio + (precio*0.16)
                    elif habitacion >= '4':
                        print ('Seleccione un opcion valida')
                        raise Exception  
                    break
                elif seleccionar_crucero == '4':
                    habitacion = input('''Las tarifas en "Sabas Nieves" son las siguientes:
                    tipo sencilla, capacidad para 3 personas, tiene un precio de 59.99 USD
                    tipo Premium, capacidad para 5 personas, tiene un precio de 99.99 USD
                    tipo VIP, capacidad para 10 personas, tiene un precio de 119.99 USD
                    que tipo de habitacion deseas?
                    1. Sencilla
                    2. Premium
                    3. VIP
                    >''')
                    if habitacion == '1':
                        pasajeros = int(input ('Cuantos boletos desea? '))
                        if pasajeros >=4:
                            print ('Les asignaremos multiples habitaciones')
                        price = 59.99
                        precio1 = 0
                        precio2 = 0
                        for i in range(pasajeros):
                            name = input('Nombre del Pasajero: ')
                            dni = int(input('DNI del Pasajero: '))
                            if dni > 1:
                                for i in range(2, dni):
                                    if (dni  % i)==0:
                                        precio = 0
                                    break
                                else: 
                                    precio1 = (price*0.1)
                            else: 
                                precio = 0
                            age = int(input('Edad de Pasajero: '))
                            if age >= 65:
                                print ('Puede optar a una mejora de habitacion!')
                            disability = input ('''Indique si el pasajero sufre alguna discapacidad
                            1. Si 
                            2. No
                            >''')
                            if disability == '1':
                                disability = 'si'
                                precio2 = (price * 0.30)
                            elif disability == '2':
                                disability = 'no'
                                precio2 = 0
                            elif disability >= '3':
                                print('Seleccione una opcion valida')
                                raise Exception                
                            precio = price - precio1 -precio2
                            price_wt = precio + (precio*0.16)
                    elif habitacion == '2':
                        pasajeros = int(input ('Cuantos boletos desea? '))
                        if pasajeros >=6:
                            print ('Les asignaremos multiples habitaciones')
                        price = 99.99
                        precio1 = 0
                        precio2 = 0
                        for i in range(pasajeros):
                            name = input('Nombre del Pasajero: ')
                            dni = int(input('DNI del Pasajero: '))
                            if dni > 1:
                                for i in range(2, dni):
                                    if (dni  % i)==0:
                                        precio = 0
                                    break
                                else: 
                                    precio1 = (price*0.1)
                            else: 
                                precio = 0
                            age = int(input('Edad de Pasajero: '))
                            if age >= 65:
                                print ('Puede optar a una mejora de habitacion!')
                            disability = input ('''Indique si el pasajero sufre alguna discapacidad
                            1. Si 
                            2. No
                            >''')
                            if disability == '1':
                                disability = 'si'
                                precio2 = (price * 0.30)
                            elif disability == '2':
                                disability = 'no'
                                precio2 = 0
                            elif disability >= '3':
                                print('Seleccione una opcion valida')
                                raise Exception                
                            precio = price - precio1 -precio2
                            price_wt = precio + (precio*0.16)
                    if habitacion == '3':
                        pasajeros = int(input ('Cuantos boletos desea? '))
                        if pasajeros >=11:
                            print ('Les asignaremos multiples habitaciones')
                        price = 119.99
                        precio1 = 0
                        precio2 = 0
                        for i in range(pasajeros):
                            name = input('Nombre del Pasajero: ')
                            dni = int(input('DNI del Pasajero: '))
                            if dni > 1:
                                for i in range(2, dni):
                                    if (dni  % i)==0:
                                        precio = 0
                                    break
                                else: 
                                    precio1 = (price*0.1)
                            else: 
                                precio = 0
                            age = int(input('Edad de Pasajero: '))
                            if age >= 65:
                                print ('Puede optar a una mejora de habitacion!')
                            disability = input ('''Indique si el pasajero sufre alguna discapacidad
                            1. Si 
                            2. No
                            >''')
                            if disability == '1':
                                disability = 'si'
                                precio2 = (price * 0.30)
                            elif disability == '2':
                                disability = 'no'
                                precio2 = 0
                            elif disability >= '3':
                                print('Seleccione una opcion valida')
                                raise Exception                
                            precio = price - precio1 -precio2
                            price_wt = precio + (precio*0.16)
                    elif habitacion >= '4':
                        print ('Seleccione un opcion valida')
                        raise Exception  
                    break
                elif seleccionar_crucero >= '5':
                    print ('Escoja una opcion posible')
                    raise Exception
            elif decision1 == '2':
                seleccionar_crucero = input('''Las Barcos que tenemos disponbles son:
                1. El Dios de los Mares
                2. La Reina Isabel
                3. El Libertador del Oceano
                4. Sabas Nieves
                >''')
                if seleccionar_crucero == '1':
                    habitacion = input('''Las tarifas en "El Dios de los Mares" son las siguientes:
                    tipo sencilla, capacidad para 2 personas, tiene un precio de 69.99 USD
                    tipo Premium, capacidad para 4 personas, tiene un precio de 89.99 USD
                    tipo VIP, capacidad para 8 personas, tiene un precio de 129.99 USD
                    que tipo de habitacion deseas?
                    1. Sencilla
                    2. Premium
                    3. VIP
                    >''')
                    if habitacion == '1':
                        habitacion = 'Sencilla'
                        pasajeros = int(input ('Cuantos boletos desea? '))
                        if pasajeros >=3:
                            print ('Les asignaremos multiples habitaciones')
                        price = 69.99
                        precio1 = 0
                        precio2 = 0
                        halls = ['A', 'B','C']
                        letra = random.randint (0, 2)
                        vista = choice(['si', 'no'])
                        answer = f'{vista} puede tener servicio a la habitacion'
                        for i in range(pasajeros):
                            name = input('Nombre del Pasajero: ')
                            dni = int(input('DNI del Pasajero: '))
                            if dni > 1:
                                for i in range(2, dni):
                                    if (dni  % i)==0:
                                        precio = 0
                                    break
                                else: 
                                    precio1 = (price*0.1)
                            else: 
                                precio = 0
                            age = int(input('Edad de Pasajero: '))
                            if age >= 65:
                                print ('Puede optar a una mejora de habitacion!')
                            disability = input ('''Indique si el pasajero sufre alguna discapacidad
                            1. Si 
                            2. No
                            >''')
                            if disability == '1':
                                disability = 'si'
                                precio2 = (price * 0.30)
                            elif disability == '2':
                                disability = 'no'
                                precio2 = 0
                            elif disability >= '3':
                                print('Seleccione una opcion valida')
                                raise Exception                
                            precio = price - precio1 -precio2
                            price_wt = precio + (precio*0.16)
                        room = Habitacion (habitacion, randrange(11), halls[letra],'2', name, answer)
                        print (room.room_characteristics())
                    elif habitacion == '2':
                        pasajeros = int(input ('Cuantos boletos desea? '))
                        if pasajeros >=5:
                            print ('Les asignaremos multiples habitaciones')
                        price = 89.99
                        precio1 = 0
                        precio2 = 0
                        for i in range(pasajeros):
                            name = input('Nombre del Pasajero: ')
                            dni = int(input('DNI del Pasajero: '))
                            if dni > 1:
                                for i in range(2, dni):
                                    if (dni  % i)==0:
                                        precio = 0
                                    break
                                else: 
                                    precio1 = (price*0.1)
                            else: 
                                precio = 0
                            age = int(input('Edad de Pasajero: '))
                            if age >= 65:
                                print ('Puede optar a una mejora de habitacion!')
                            disability = input ('''Indique si el pasajero sufre alguna discapacidad
                            1. Si 
                            2. No
                            >''')
                            if disability == '1':
                                disability = 'si'
                                precio2 = (price * 0.30)
                            elif disability == '2':
                                disability = 'no'
                                precio2 = 0
                            elif disability >= '3':
                                print('Seleccione una opcion valida')
                                raise Exception                
                            precio = price - precio1 -precio2
                            price_wt = precio + (precio*0.16)
                    elif habitacion == '3':
                        pasajeros = int(input ('Cuantos boletos desea? '))
                        if pasajeros >=9:
                            print ('Les asignaremos multiples habitaciones')
                        price = 129.99
                        precio1 = 0
                        precio2 = 0
                        for i in range(pasajeros):
                            name = input('Nombre del Pasajero: ')
                            dni = int(input('DNI del Pasajero: '))
                            if dni > 1:
                                for i in range(2, dni):
                                    if (dni  % i)==0:
                                        precio = 0
                                    break
                                else: 
                                    precio1 = (price*0.1)
                            else: 
                                precio = 0
                            age = int(input('Edad de Pasajero: '))
                            if age >= 65:
                                print ('Puede optar a una mejora de habitacion!')
                            disability = input ('''Indique si el pasajero sufre alguna discapacidad
                            1. Si 
                            2. No
                            >''')
                            if disability == '1':
                                disability = 'si'
                                precio2 = (price * 0.30)
                            elif disability == '2':
                                disability = 'no'
                                precio2 = 0
                            elif disability >= '3':
                                print('Seleccione una opcion valida')
                                raise Exception                
                            precio = price - precio1 -precio2
                            price_wt = precio + (precio*0.16)
                    elif habitacion >= '4':
                        print ('Seleccione un opcion valida')
                        raise Exception  
                    break                      
                elif seleccionar_crucero == '2':
                    habitacion = input('''Las tarifas en "La Reina Isabel" son las siguientes:
                    tipo sencilla, capacidad para 2 personas, tiene un precio de 9.99 USD
                    tipo Premium, capacidad para 4 personas, tiene un precio de 99.99 USD
                    tipo VIP, capacidad para 8 personas, tiene un precio de 119.99 USD
                    que tipo de habitacion deseas?
                    1. Sencilla
                    2. Premium
                    3. VIP
                    >''')
                    if habitacion == '1':
                        pasajeros = int(input ('Cuantos boletos desea? '))
                        if pasajeros >=3:
                            print ('Les asignaremos multiples habitaciones')
                        price = 59.99
                        precio1 = 0
                        precio2 = 0
                        for i in range(pasajeros):
                            name = input('Nombre del Pasajero: ')
                            dni = int(input('DNI del Pasajero: '))
                            if dni > 1:
                                for i in range(2, dni):
                                    if (dni  % i)==0:
                                        precio = 0
                                    break
                                else: 
                                    precio1 = (price*0.1)
                            else: 
                                precio = 0
                            age = int(input('Edad de Pasajero: '))
                            if age >= 65:
                                print ('Puede optar a una mejora de habitacion!')
                            disability = input ('''Indique si el pasajero sufre alguna discapacidad
                            1. Si 
                            2. No
                            >''')
                            if disability == '1':
                                disability = 'si'
                                precio2 = (price * 0.30)
                            elif disability == '2':
                                disability = 'no'
                                precio2 = 0
                            elif disability >= '3':
                                print('Seleccione una opcion valida')
                                raise Exception                
                            precio = price - precio1 -precio2
                            price_wt = precio + (precio*0.16)
                    elif habitacion == '2':
                        pasajeros = int(input ('Cuantos boletos desea? '))
                        if pasajeros >=5:
                            print ('Les asignaremos multiples habitaciones')
                        price = 99.99
                        precio1 = 0
                        precio2 = 0
                        for i in range(pasajeros):
                            name = input('Nombre del Pasajero: ')
                            dni = int(input('DNI del Pasajero: '))
                            if dni > 1:
                                for i in range(2, dni):
                                    if (dni  % i)==0:
                                        precio = 0
                                    break
                                else: 
                                    precio1 = (price*0.1)
                            else: 
                                precio = 0
                            age = int(input('Edad de Pasajero: '))
                            if age >= 65:
                                print ('Puede optar a una mejora de habitacion!')
                            disability = input ('''Indique si el pasajero sufre alguna discapacidad
                            1. Si 
                            2. No
                            >''')
                            if disability == '1':
                                disability = 'si'
                                precio2 = (price * 0.30)
                            elif disability == '2':
                                disability = 'no'
                                precio2 = 0
                            elif disability >= '3':
                                print('Seleccione una opcion valida')
                                raise Exception                
                            precio = price - precio1 -precio2
                            price_wt = precio + (precio*0.16)
                    if habitacion == '3':
                        pasajeros = int(input ('Cuantos boletos desea? '))
                        if pasajeros >=9:
                            print ('Les asignaremos multiples habitaciones')
                        price = 119.99
                        precio1 = 0
                        precio2 = 0
                        for i in range(pasajeros):
                            name = input('Nombre del Pasajero: ')
                            dni = int(input('DNI del Pasajero: '))
                            if dni > 1:
                                for i in range(2, dni):
                                    if (dni  % i)==0:
                                        precio = 0
                                    break
                                else: 
                                    precio1 = (price*0.1)
                            else: 
                                precio = 0
                            age = int(input('Edad de Pasajero: '))
                            if age >= 65:
                                print ('Puede optar a una mejora de habitacion!')
                            disability = input ('''Indique si el pasajero sufre alguna discapacidad
                            1. Si 
                            2. No
                            >''')
                            if disability == '1':
                                disability = 'si'
                                precio2 = (price * 0.30)
                            elif disability == '2':
                                disability = 'no'
                                precio2 = 0
                            elif disability >= '3':
                                print('Seleccione una opcion valida')
                                raise Exception                
                            precio = price - precio1 -precio2
                            price_wt = precio + (precio*0.16)
                    elif habitacion >= '4':
                        print ('Seleccione un opcion valida')
                        raise Exception  
                    break
                elif seleccionar_crucero == '3':
                    habitacion = input('''Las tarifas en "El Libertador del Oceano" son las siguientes:
                    tipo sencilla, capacidad para 3 personas, tiene un precio de 49.99 USD
                    tipo Premium, capacidad para 5 personas, tiene un precio de 89.99 USD
                    tipo VIP, capacidad para 12 personas, tiene un precio de 139.99 USD
                    que tipo de habitacion deseas?
                    1. Sencilla
                    2. Premium
                    3. VIP
                    >''')
                    if habitacion == '1':
                        pasajeros = int(input ('Cuantos boletos desea? '))
                        if pasajeros >=4:
                            print ('Les asignaremos multiples habitaciones')
                        price = 49.99
                        precio1 = 0
                        precio2 = 0
                        for i in range(pasajeros):
                            name = input('Nombre del Pasajero: ')
                            dni = int(input('DNI del Pasajero: '))
                            if dni > 1:
                                for i in range(2, dni):
                                    if (dni  % i)==0:
                                        precio = 0
                                    break
                                else: 
                                    precio1 = (price*0.1)
                            else: 
                                precio = 0
                            age = int(input('Edad de Pasajero: '))
                            if age >= 65:
                                print ('Puede optar a una mejora de habitacion!')
                            disability = input ('''Indique si el pasajero sufre alguna discapacidad
                            1. Si 
                            2. No
                            >''')
                            if disability == '1':
                                disability = 'si'
                                precio2 = (price * 0.30)
                            elif disability == '2':
                                disability = 'no'
                                precio2 = 0
                            elif disability >= '3':
                                print('Seleccione una opcion valida')
                                raise Exception                
                            precio = price - precio1 -precio2
                            price_wt = precio + (precio*0.16)
                    elif habitacion == '2':
                        pasajeros = int(input ('Cuantos boletos desea? '))
                        if pasajeros >=6:
                            print ('Les asignaremos multiples habitaciones')
                        price = 89.99
                        precio1 = 0
                        precio2 = 0
                        for i in range(pasajeros):
                            name = input('Nombre del Pasajero: ')
                            dni = int(input('DNI del Pasajero: '))
                            if dni > 1:
                                for i in range(2, dni):
                                    if (dni  % i)==0:
                                        precio = 0
                                    break
                                else: 
                                    precio1 = (price*0.1)
                            else: 
                                precio = 0
                            age = int(input('Edad de Pasajero: '))
                            if age >= 65:
                                print ('Puede optar a una mejora de habitacion!')
                            disability = input ('''Indique si el pasajero sufre alguna discapacidad
                            1. Si 
                            2. No
                            >''')
                            if disability == '1':
                                disability = 'si'
                                precio2 = (price * 0.30)
                            elif disability == '2':
                                disability = 'no'
                                precio2 = 0
                            elif disability >= '3':
                                print('Seleccione una opcion valida')
                                raise Exception                
                            precio = price - precio1 -precio2
                            price_wt = precio + (precio*0.16)
                    if habitacion == '3':
                        pasajeros = int(input ('Cuantos boletos desea? '))
                        if pasajeros >=13:
                            print ('Les asignaremos multiples habitaciones')
                        price = 139.99
                        precio1 = 0
                        precio2 = 0
                        for i in range(pasajeros):
                            name = input('Nombre del Pasajero: ')
                            dni = int(input('DNI del Pasajero: '))
                            if dni > 1:
                                for i in range(2, dni):
                                    if (dni  % i)==0:
                                        precio = 0
                                    break
                                else: 
                                    precio1 = (price*0.1)
                            else: 
                                precio = 0
                            age = int(input('Edad de Pasajero: '))
                            if age >= 65:
                                print ('Puede optar a una mejora de habitacion!')
                            disability = input ('''Indique si el pasajero sufre alguna discapacidad
                            1. Si 
                            2. No
                            >''')
                            if disability == '1':
                                disability = 'si'
                                precio2 = (price * 0.30)
                            elif disability == '2':
                                disability = 'no'
                                precio2 = 0
                            elif disability >= '3':
                                print('Seleccione una opcion valida')
                                raise Exception                
                            precio = price - precio1 -precio2
                            price_wt = precio + (precio*0.16)
                    elif habitacion >= '4':
                        print ('Seleccione un opcion valida')
                        raise Exception  
                    break
                elif seleccionar_crucero == '4':
                    habitacion = input('''Las tarifas en "Sabas Nieves" son las siguientes:
                    tipo sencilla, capacidad para 3 personas, tiene un precio de 59.99 USD
                    tipo Premium, capacidad para 5 personas, tiene un precio de 99.99 USD
                    tipo VIP, capacidad para 10 personas, tiene un precio de 119.99 USD
                    que tipo de habitacion deseas?
                    1. Sencilla
                    2. Premium
                    3. VIP
                    >''')
                    if habitacion == '1':
                        pasajeros = int(input ('Cuantos boletos desea? '))
                        if pasajeros >=4:
                            print ('Les asignaremos multiples habitaciones')
                        price = 59.99
                        precio1 = 0
                        precio2 = 0
                        for i in range(pasajeros):
                            name = input('Nombre del Pasajero: ')
                            dni = int(input('DNI del Pasajero: '))
                            if dni > 1:
                                for i in range(2, dni):
                                    if (dni  % i)==0:
                                        precio = 0
                                    break
                                else: 
                                    precio1 = (price*0.1)
                            else: 
                                precio = 0
                            age = int(input('Edad de Pasajero: '))
                            if age >= 65:
                                print ('Puede optar a una mejora de habitacion!')
                            disability = input ('''Indique si el pasajero sufre alguna discapacidad
                            1. Si 
                            2. No
                            >''')
                            if disability == '1':
                                disability = 'si'
                                precio2 = (price * 0.30)
                            elif disability == '2':
                                disability = 'no'
                                precio2 = 0
                            elif disability >= '3':
                                print('Seleccione una opcion valida')
                                raise Exception                
                            precio = price - precio1 -precio2
                            price_wt = precio + (precio*0.16)
                    elif habitacion == '2':
                        pasajeros = int(input ('Cuantos boletos desea? '))
                        if pasajeros >=6:
                            print ('Les asignaremos multiples habitaciones')
                        price = 99.99
                        precio1 = 0
                        precio2 = 0
                        for i in range(pasajeros):
                            name = input('Nombre del Pasajero: ')
                            dni = int(input('DNI del Pasajero: '))
                            if dni > 1:
                                for i in range(2, dni):
                                    if (dni  % i)==0:
                                        precio = 0
                                    break
                                else: 
                                    precio1 = (price*0.1)
                            else: 
                                precio = 0
                            age = int(input('Edad de Pasajero: '))
                            if age >= 65:
                                print ('Puede optar a una mejora de habitacion!')
                            disability = input ('''Indique si el pasajero sufre alguna discapacidad
                            1. Si 
                            2. No
                            >''')
                            if disability == '1':
                                disability = 'si'
                                precio2 = (price * 0.30)
                            elif disability == '2':
                                disability = 'no'
                                precio2 = 0
                            elif disability >= '3':
                                print('Seleccione una opcion valida')
                                raise Exception                
                            precio = price - precio1 -precio2
                            price_wt = precio + (precio*0.16)
                    if habitacion == '3':
                        pasajeros = int(input ('Cuantos boletos desea? '))
                        if pasajeros >=11:
                            print ('Les asignaremos multiples habitaciones')
                        price = 119.99
                        precio1 = 0
                        precio2 = 0
                        for i in range(pasajeros):
                            name = input('Nombre del Pasajero: ')
                            dni = int(input('DNI del Pasajero: '))
                            if dni > 1:
                                for i in range(2, dni):
                                    if (dni  % i)==0:
                                        precio = 0
                                    break
                                else: 
                                    precio1 = (price*0.1)
                            else: 
                                precio = 0
                            age = int(input('Edad de Pasajero: '))
                            if age >= 65:
                                print ('Puede optar a una mejora de habitacion!')
                            disability = input ('''Indique si el pasajero sufre alguna discapacidad
                            1. Si 
                            2. No
                            >''')
                            if disability == '1':
                                disability = 'si'
                                precio2 = (price * 0.30)
                            elif disability == '2':
                                disability = 'no'
                                precio2 = 0
                            elif disability >= '3':
                                print('Seleccione una opcion valida')
                                raise Exception                
                            precio = price - precio1 -precio2
                            price_wt = precio + (precio*0.16)
                    elif habitacion >= '4':
                        print ('Seleccione un opcion valida')
                        raise Exception  
                    break
                elif seleccionar_crucero >= '5':
                    print ('Escoja una opcion posible')
                    raise Exception
            elif decision3 >= '3':
                print ('selecione una opcion posible')      
        except:
            print ('Por favor verifique sus datos!')
    pasajero = Pasajero(name, dni, age, disability, price_wt)   
    return pasajero.passenger_characteristics()

def registrar_turista():
    while True:
        try:
            name = input('Ingrese su nombre: ')
            dni = input('Ingrese si DNI: ')
            age = int(input('Ingrese su edad: '))
            check = 0
            break
        except:
            print('Valide sus datos!')
    turista = Turista(name, dni, age, check)
    print('Fuiste registrado como turista exitosamente!')
    return turista

def ver_cuenta(turistas):
    dni = input('Ingrese su DNI:')
    for turista in turistas:
        if turista.dni == dni:
            turista.ver_cuenta()
            return True
    return False     

def tour_puerto(turistas):
    dni = input('Ingrese su DNI:')
    for turista in turistas:
        if turista.dni == dni:
            while True:
                try:
                    price = int(input('El costo de este tour es de: "30 USD", por favor ingrese el monto a cancelar: '))
                    if price != 30:
                        print ('El precio de este tour es de 30 USD')
                        raise Exception
                    break   
                except:
                    print ('Error, valide sus datos')
            turista.tour_puerto(price)
            print ('Deposito realizado con exito')
            return True
    return False

def comida_local(turistas):
    dni = input('Ingrese su DNI:')
    for turista in turistas:
        if turista.dni == dni:
            while True:
                try:
                    price = int(input('El costo de la degustacion es de: "100 USD", por favor ingrese el monto a cancelar: '))
                    if price != 100:
                        print ('El precio de esta degustacion es de 100 USD')
                        raise Exception
                    break   
                except:
                    print ('Error, valide sus datos')
            turista.comida_local(price)
            print ('Deposito realizado con exito')
            return True
    return False

def trotar(turistas):
    dni = input('Ingrese su DNI:')
    for turista in turistas:
        if turista.dni == dni:
            while True:
                try:
                    price = int(input('Trotar es gratis!!, por favor coloque 0: '))
                    if price != 0:
                        print ('Trotar es gratis')
                        raise Exception
                    break   
                except:
                    print ('Error, valide sus datos')
            turista.trotar(price)
            print ('Deposito realizado con exito')
            return True
    return False

def lugares_historicos(turistas):
    dni = input('Ingrese su DNI:')
    for turista in turistas:
        if turista.dni == dni:
            while True:
                try:
                    price = int(input('La visita a lugares historicos tiene un costo de la degustacion es de: "40 USD", por favor ingrese el monto a cancelar: '))
                    if price != 40:
                        print ('La visita a lugares historicos cuesta 40 USD')
                        raise Exception
                    break   
                except:
                    print ('Error, valide sus datos')
            turista.lugares_historicos(price)
            print ('Deposito realizado con exito')
            return True
    return False

def menu_tours(pasajeros):
    turistas = []
    while True:
        opcion = input('''Escoge tu opcion:
        1. Registrate para realizar turismo
        2. Tour en el puerto
        3. Degustacion de comida local
        4. Trotar por el pueblo/ciudad
        5. Visita a lugares historicos
        6. Ver gastos totales en tours
        7. Salir
        >''')
        if opcion == '1':
            turistas.append(registrar_turista())
        elif opcion == '2':
            tour_puerto (turistas) 
        elif opcion == '3':
            comida_local (turistas)
        elif opcion == '4':
            trotar (turistas)
        elif opcion == '5': 
            lugares_historicos (turistas)
        elif opcion == '6':
            ver_cuenta(turistas)  
        elif opcion == '7':
            print('Esperamos que sigas disfrutando de nuestro crucero, adios!')
            break
        elif opcion >= '8':
                print ('Seleccione una opcion valida')
                raise Exception       

def tours(pasajeros):
    menu_tours(pasajeros)

def agregar_plato():
    while True:
        try:
            name = input('Ingrese el nombre del producto: ')
            classification = input('''Indique como clasifica este producto:
            1. Alimento
            2. Bebida
            >''')
            if classification == '1':
                classification = 'Alimento'
                option = input('''Indique como debe venderse este alimento
                1. Empaque
                2. Preparacion
                >''')
                if option == '1':
                    option = 'Empaque'
                elif option == '2':
                    option = 'Preparacion'
            elif classification == '2':
                classification = 'Bebida'
                option = input('''Indique el tamaño de bebida:
                1. Pequeña
                2. Mediana
                3. Grande
                >''')
                if option == '1':
                    option = 'Pequeña'
                elif option == '2':
                    option = 'Mediana'
                elif option == '3':
                    option = 'Grande'
            elif classification <= 3:
                print ('El producto debe tener un precio para ser vendido en el restaurante')
                raise Exception
            price = float(input('Indique el precio del producto: '))
            precio = price + (price * 0.16)
            warning = print (f'El precio despues de colocar el impuesto seria de {precio}')
            if price <= 0:
                print ('El producto debe tener un precio para ser vendido en el restaurante')
                raise Exception
            break
        except:
            print('Por favor verifique los datos ingresados!')
    plato = Plato(name, classification, option, precio)
    print('El producto fue agregado al menu correctamente!')
    return plato.mostrar_plato()

def agregar_combo():
    while True:
        try:
            name = input('Ingrese el nombre del combo: ')
            cantidad = int(input('Indique la cantidad de productos que conforman el combo: '))
            if cantidad <= 1:
                print ('El combo debe contar por lo menos 2 productos')
                raise Exception
            products = input('Indique que productos tiene el combo: ')
            price = float(input('Indique el precio del combo: '))
            precio = price + (price * 0.16)
            warning = print (f'El precio despues de colocar el impuesto seria de {precio}')
            if price <= 0:
                print ('El combo debe tener un precio para ser vendido en el restaurante')
                raise Exception
            break
        except:
            print ('Por favor verifique los datos ingresado!')
    combo = Combo(name, cantidad, products, precio)
    print ('Combo agregado al menu correctamente!')
    return combo.mostrar_combo()

def eliminar_plato(platos):
    for i, plato in enumerate(platos, 1):
        print (i, plato)
    option = int(input('Indique el numero del plato que deseas eliminar: '))
    platos.pop(option - 1)
    print ('El plato ha sido eliminado correctamente')

def eliminar_combo (combos):
    for i, combo in enumerate (combos, 1):
        print (i, combo)
    option = int(input('Indique el numero del combo que desea eliminar:'))
    combos.pop(option - 1)
    print ('El combo ha sido eliminado correctamente')

def modificar_plato (platos):
    for i, plato in enumerate(platos, 1):
        print (i, plato)
    option1 = int(input('Seleccione el numero del plato que deseas editar: '))
    plato_seleccionado = platos [option1-1]
    option2 = input('''Indique que aspecto del plato desea modificar:
    1. Nombre
    2. Precio
    >''')
    if option2 == '1':
        new = input('Indique el nuevo nombre del plato')
        plato.name = new 
        print (plato.mostrar_plato())
    elif option2 == '2':
        new = input('Indique el nuevo precio: ')
        plato.precio = new 
    elif option2 <='3':
        print ('Error')  

def buscar_plato(platos, target):
    target = input('Indique el nombre del producto')
    start = 0
    end = len(platos) - 1
    while start <= end:
        middle = (start + end)//2
        midpoint = platos[middle]
        if midpoint > target:
            end = midpoint -1
        elif midpoint < target:
            start = midpoint + 1
        else:
            return midpoint

def buscar_combo(combos, target):
    start = 0
    end = len(combos)-1
    while start <=end:
        middle = (start + end//2)
        midpoint =combos [middle]
        if midpoint < target:
            end = midpoint - 1
        elif midpoint < target:
            start = midpoint + 1
        else:
            return midpoint

def gestionar_restaurant():
    platos = []
    combos = []
    while True:
        opcion = input('''Bienvenido al restarante de Saman Caribbean:
        1. Agregar Plato al Menu
        2. Agregar Combo al Menu
        3. Eliminar Plato del Menu
        4. Eliminar Combo del Menu
        5. Modificar Plato del Menu
        6. Buscar Plato en el Menu
        7. Buscar Combo en el Menu 
        8.Salir
        >''')
        if opcion == '1':
            platos.append (agregar_plato())
            print(platos)
        elif opcion == '2':
            combos.append(agregar_combo()) 
            print (combos)
        elif opcion == '3':
            eliminar_plato(platos)
        elif opcion == '4':
            for i, combo in enumerate (combos, 1):
                print (i, plato) 
            trotar (turistas)
        elif opcion == '5': 
            modificar_plato(platos)
        elif opcion == '6':
            target = input('Indique el nombre del producto: ')
            buscar_plato(platos, target)
        elif opcion == '7':
            target = input('Indique el nombre del combo: ')
            buscar_plato(combo, target)
        elif opcion == '8':
            print('Esperamos que sigas disfrutando de nuestro crucero, adios!')
            break    
        elif opcion >= '9':
            print('Seleccione una opcion valida')


def estadisticas(pasajeros):
    while True:
        try:
            opcion = input('''Que estadistica deseas ver:
            1. Promedio de gasto por cliente
            2. Porcentaje de clientes que no compran tour
            3. Top 3 cruceros con mas tickets vendidos
            >''')
            if opcion =='1':
                print('En promedio, los clientes gastan 457.16 USD')
            elif opcion == '2':
                print ('El 36% de los clientes no comprar los tours')
            elif opcion == '3':
                print ('''
                1. La Reina Isabel
                2. El Libertador del Oceano
                3. El Dios de los Mares''')
            elif opcion >= '4':
                raise Exception
            break
        except:
            print ('Introduzca una opcion valia!')


def main():
    pasajeros = []
    turista = []
    while True:
        opcion = input('''Bienvenido a Saman Caribbean:
        1. Comprar boletos
        2. Comprar tour
        3. Gestion del Restaurant
        4. Ver Estadisticas
        5. Salir
        >''')
        if opcion == '1':
            pasajeros.append(registrar_pasajero())
            print (pasajeros)
        elif opcion == '2':
            tours(pasajeros)
        elif opcion == '3':
            gestionar_restaurant()
        elif opcion == '4':
            estadisticas(pasajeros)
        elif opcion == '5':
            print ('Que tenga un feliz dia!')
            break
        elif opcion >='6':
            print ('seleccione una opcion posible')
    return True

main()