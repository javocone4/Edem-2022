class Cliente():
    #Atributos, NIF (string), nombre (string), apellidos (string), teléfono (string), email (string) y preferente (boolean)
    def __init__(self,nif,nombre,apell,tlfn,email,preferente):
        self.nif = nif
        self.nombre = nombre
        self.apell = apell
        self.tlfn = tlfn
        self.email = email
        self.preferente = preferente
lista = []    
def funcion():
    print("Bienvenido a la gestión de los clientes en la Empresa.")
    while True:
        print("\nSi quiere añadir un cliente pulse 1.\nSi quiere eliminar un cliente pulse 2.\nSi quiere mostrar un cliente pulse 3.\nSi quiere listar todos los clientes pulse 4.\nSi quiere mostrar los clientes preferentes pulse 5.\nSi quiere salir del programa pulse 6.\n")
        number = int(input("Elige un número: "))
        
        if number == 1:
            print("\nAñadir un cliente.\n")
            nif:str =input("DNI: ")
            nombre:str  =input("Nombre: ")
            apell:str  =input("Apellido: ")
            tlf:str  =input("Teléfono: ")
            email :str =input("Email: ")
            preferente:bool =input("Preferente(elige yes o no): ")
        
            cliente = Cliente(nif,nombre,apell,tlf,email,preferente)
            lista.append(cliente)
            print("\nCliente añadido.\n")
            
        
        elif number ==2:
            print("Eliminar cliente.\n")
            dni1 = str(input('Introduzca el DNI del cliente a eliminar: '))
            for cliente in lista:
                    if cliente.nif == dni1:
                        lista.remove(cliente)
                        print('\nEl cliente ha sido eliminado')
                    else:
                        print('\nEl DNI introducido es incorrecto.')

        elif number ==3:
            print("Listar cliente")         
            dni1 = str(input('Introduzca el DNI del cliente a encontrar: '))
            for cliente in lista:
                if cliente.nif == dni1:
                    print(f'\nDNI: {dni1}\nNombre: {cliente.nombre}\nApellidos: {cliente.apell}\nTelefono: {cliente.tlfn}\nEmail:{cliente.email}\nPreferente: {cliente.preferente}')
                    break
                else:
                    print('El DNI no existe.')
                    
        
        elif number ==4:
            print('Mostrar todos los clientes.')
            for cliente in lista:
                print(f'\nDNI: {cliente.nif}\nNombre: {cliente.nombre}\nApellidos: {cliente.apell}\nTelefono: {cliente.tlfn}\nEmail:{cliente.email}\nPreferente: {cliente.preferente}')
        elif number ==5:
            print('Mostrar clientes preferentes.')
            for cliente in lista:
                if cliente.preferente == 'yes':
                    print(f'\nDNI: {cliente.nif}\nNombre: {cliente.nombre}\nApellidos: {cliente.apell}\nTelefono: {cliente.tlfn}\nEmail:{cliente.email}\nPreferente: {cliente.preferente}')
        elif number ==6:
            print("Saliendo del programa...")
            break
      
funcion()
    
            