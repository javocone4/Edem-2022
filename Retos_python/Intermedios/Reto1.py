from datetime import date


def reto1():
    lista = []
    disc1 = {
        "nombre": "Un verano sin ti",
        "artista": "Bad Bunny",
        "año": 2022,
        "precio": 15,
        "genero": "Reggaeton"
    }

    disc2 = {
        "nombre": "Motomami",
        "artista": "Rosalía",
        "año": 2022,
        "precio": 18,
        "genero": "Pop"
    }

    disc3 = {
        "nombre": "Hollywood's Bleeding",
        "artista": "Post Malone",
        "año": 2019,
        "precio": 13,
        "genero": "Pop"
    }

    disc4 = {
        "nombre": "Dig your own hole",
        "artista": "The Chemical Brothers",
        "año": 1997,
        "precio": 13,
        "genero": "Electro"
    }

    disc5 = {
        "nombre": "At the heart of winter",
        "artista": "Immortal",
        "año": 1999,
        "precio": 15,
        "genero": "Black metal"
    }
    lista = [disc1, disc2, disc3, disc4, disc5]
    lista1 = []
    number = int(
        input(
            "¿Qué disco le gustaria comprar?\nElige: 1, si quiere ver los discos disponibles\nElige: 0, si quiere salir\n"
        ))

    if number == 0:
        print("Adiós, que tenga un buen día")
        exit()
    else:
        print("\nDiscos disponibles, elige el número del que quieras:\n")
        j = 0
        for n in lista:
            j += 1
            for k, v in n.items():
                if k == "nombre":
                    print(j, v)
                    lista1.append(v)
        
      
        numero = int(input())

        if numero == 0:
          for n in lista:
            j += 1
            for k, v in n.items():
                if k == "nombre":
                    print(j, v)
        elif numero == 1:
              dic = disc1["nombre"]
              print(
                  "Este álbum tiene un precio de 15 euros.\nPulsa la tecla cero para el ticket."
              )
        elif numero == 2:
              dic = disc2["nombre"]
              print(
                  "Este álbum tiene un precio de 18 euros.\nPulsa la tecla cero para el ticket."
              )
        elif numero == 3:
              dic = disc3["nombre"]
              print(
                  "Este álbum tiene un precio de 13 euros.\nPulsa la tecla cero para el ticket."
              )
        elif numero == 4:
              dic = disc4["nombre"]
              print(
                  "Este álbum tiene un precio de 9,1 euros, ya que esta rebajado.\nPulsa la tecla cero para el ticket."
              )
        elif numero == 5:
              dic = disc5["nombre"]
              print(
                  "Este álbum tiene un precio de 10,5 euros, ya que esta rebajado.\nPulsa la tecla cero para el ticket."
              )
        numero1 = int(input())
        if numero1 == 0:
            print(f"Gracias por su compra. Su disco nuevo es {dic}")
            dia = date.today()
            print(f"Fecha de compra: {dia}")
