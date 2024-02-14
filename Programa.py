from Funciones import *
import time

listacines = leer_json()

numero = menu()
while numero != 6:
    if numero == 1:
        cines, ubicacion, telefonos = listar_informacion(listacines)
        print("Se encuentran los siguientes cines: ")
        for cine, ubicacion, telefono in zip(cines, ubicacion, telefonos):
            print("\nCine:", cine, "\nUbicación:", ubicacion, "\nTeléfono:", telefono)
            esperar_continuar()

    elif numero == 2:
        pelis, generos = contar_informacion(listacines)
        print("La cantidad de películas almacenadas es: ", len(pelis))
        for peli, genero in zip(pelis, generos):
            print("\nTítulo:", peli, "\nGénero/s:", ','.join(genero))
            esperar_continuar()

    elif numero == 3:
        director, anyoestreno = filtrar_informacion(listacines)
        if director == False and anyoestreno == False:
            print("Película no encontrada")
            esperar_continuar()
        else:
            print("\nDirector:", director, "\nAño de estreno:", anyoestreno)
            esperar_continuar()

    elif numero == 4:
        titulopeli, resumen = buscar_informacion_relacionada(listacines)
        print("La cantidad de películas con esta valoración es:", len(titulopeli))
        for peli, sinopsis in zip(titulopeli, resumen):
            print("\nTítulo:", peli, "\nSinopsis:", sinopsis)
            esperar_continuar()

    elif numero == 5:
        sino = ejercicio_libre(listacines)
        if sino == False:
            print("Película no encontrada.")
            esperar_continuar()
        else:
            print("Sinopsis:", sino)
            esperar_continuar()

    numero = menu()

if numero == 6:
    print("Saliendo...")
    time.sleep(2)
    

