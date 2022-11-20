from datetime import date


def reto1():
    discos = {

        'disc1' :{      
            "nombre": "Un verano sin ti",
            "artista": "Bad Bunny",
            "año": 2022,
            "precio": 15,
            "genero": "Reggaeton"
        },

        'disc2' :{
            "nombre": "Motomami",
            "artista": "Rosalía",
            "año": 2022,
            "precio": 18,
            "genero": "Pop"
        },

        'disc3' : {
            "nombre": "Hollywood's Bleeding",
            "artista": "Post Malone",
            "año": 2019,
            "precio": 13,
            "genero": "Pop"
        },

        'disc4' : {
            "nombre": "Dig your own hole",
            "artista": "The Chemical Brothers",
            "año": 1997,
            "precio": 13,
            "genero": "Electro"
        },

        'disc5' : {
            "nombre": "At the heart of winter",
            "artista": "Immortal",
            "año": 1999,
            "precio": 15,
            "genero": "Black metal"
        }
    }
    number = int(
        input(
            "¿Qué disco le gustaria comprar?\nElige: 1, si quiere ver los discos disponibles\nElige: 0, si quiere salir\n"
        ))

    if number == 0:
        print("Adiós, que tenga un buen día")
        exit()
    else:
        print("\nDiscos disponibles, elige el número del que quieras:\n")
        for i, disco in discos.items():  
            nombredisco = i
            nombre = disco['nombre']
            artista = disco['artista']
            anio = disco['año']
            precio = disco['precio']
            genero = disco['genero']

            print(f"Disco: {nombredisco}\nNombre: {nombre} \naAtista: {artista} \nAño: {anio} \nPrecio: {precio}\nGénero: {genero}\n\n")

        elegirDisco = input("Elige el disco que desee:\n ") 

        if elegirDisco == 'disc1':
            print(f'Ha elegido el disco {elegirDisco}.')
            nombre = discos['disc1'].get('nombre')
            artista = discos['disc1'].get('artista')
            precio = discos['disc1'].get('precio') 
            fecha = date.today()
            print(f"\nTicket de la compra\nDisco: {nombre}\nArtista: {artista}\nFecha de compra: {fecha}\nPrecio: {precio}€")
        elif elegirDisco == 'disc2':
            print(f'Ha elegido el disco {elegirDisco}.')
            nombre = discos['disc2'].get('nombre')
            artista = discos['disc2'].get('artista')
            precio = discos['disc2'].get('precio') 
            fecha = date.today()
            print(f"\nTicket de la compra\nDisco: {nombre}\nArtista: {artista}\nFecha de compra: {fecha}\nPrecio: {precio}€")
        elif elegirDisco == 'disc3':
            print(f'Ha elegido el disco {elegirDisco}.')
            nombre = discos['disc3'].get('nombre')
            artista = discos['disc3'].get('artista')
            precio = discos['disc3'].get('precio') 
            fecha = date.today()
            print(f"\nTicket de la compra\nDisco: {nombre}\nArtista: {artista}\nFecha de compra: {fecha}\nPrecio: {precio}€")
        elif elegirDisco == 'disc4':
            print(f'Ha elegido el disco {elegirDisco}.')
            nombre = discos['disc4'].get('nombre')
            artista = discos['disc4'].get('artista')
            precio = discos['disc4'].get('precio') * 0,75
            fecha = date.today()
            print(f"\nTicket de la compra\nDisco: {nombre}\nArtista: {artista}\nFecha de compra: {fecha}\nPrecio: {precio}€\nCon este disco te has ahorrado un 30%")
        elif elegirDisco == 'disc5':
            print(f'Ha elegido el disco {elegirDisco}.')
            nombre = discos['disc5'].get('nombre')
            artista = discos['disc5'].get('artista')
            precio = discos['disc5'].get('precio') *0.75
            fecha = date.today()
            print(f"\nTicket de la compra\nDisco: {nombre}\nArtista: {artista}\nFecha de compra: {fecha}\nPrecio: {precio}€\nCon este disco te has ahorrado un 30%")
        
reto1()
