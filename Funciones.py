import json
import datetime

def leer_json():
    with open("Cines.json") as f:
        datos = json.load(f)
    return datos

def menu():
    menu = """
    ----------------------------------------
    1. Listar información.                  
    2. Contar información.                  
    3. Buscar o filtrar información         
    4. Buscar información relacionada.      
    5. Ejercicio libre.                                 
    6. Salir                                
    ----------------------------------------
    """ 
    print(menu)
    while True:
        try:
            numero = int(input("Elije una de las opciones anteriores: "))
            if 1 <= numero <= 6:
                return numero
            else:
                print("Debe ser un número de los de la lista")
        except ValueError:
            print("Por favor, introduce un número.")

def listar_informacion(listacines):
    cines = []
    ubicacion = []
    telefono = []
    for cine_info in listacines.get("cines").values():
        cines.append(cine_info["nombre"])
        ubicacion.append(cine_info["direccion"])
        telefono.append(cine_info["telefono"])
    return cines, ubicacion, telefono

def contar_informacion(listacines):
    pelicula = []
    generos = []
    for pelicula_info in listacines.get("peliculas").values():
        pelicula.append(pelicula_info["titulo"])
        generos.append(pelicula_info["genero"])
    return pelicula, generos

def filtrar_informacion(listacines):
    titulospelis = [pelicula_info["titulo"] for pelicula_info in listacines.get("peliculas").values()]
    print(','.join(titulospelis))
    peliculateclado = input("Introduce el nombre de la película a consultar: ")
    if peliculateclado not in titulospelis:
        return False, False
    else:
        for pelicula_info in listacines.get("peliculas").values():
            if pelicula_info["titulo"] == peliculateclado:
                director = pelicula_info["director"]
                anyoestreno = pelicula_info["year"]
                return director, anyoestreno

def buscar_informacion_relacionada(listacines):
    pelisvaloradas = []
    sinopsis = []
    valoracion = int(input("Introduce el número sobre 5 de valoración de la película: "))
    while valoracion < 1 or valoracion > 5:
        print("Debe ser un número del 1 al 5")
        valoracion = int(input("Introduce el número de valoración: "))
    for pelicula_info in listacines.get("peliculas").values():
        if pelicula_info["valoracion"] == valoracion:
            pelisvaloradas.append(pelicula_info["titulo"])
            sinopsis.append(pelicula_info["sipnosis"])
    return pelisvaloradas, sinopsis

def mostrar_hora():
    hora = datetime.datetime.now()
    hora_formato = hora.strftime('%H:%M')
    return hora_formato

def ejercicio_libre(listacines):
    generos = set()
    titulos = []
    for pelicula_info in listacines.get("peliculas").values():
        generos.update(pelicula_info["genero"])
    print(','.join(generos))
    generoteclado = input("Introduce un género de los mostrados anteriormente: ")
    if generoteclado not in generos:
        print("Género no válido, saliendo")
        return False
    else:
        for pelicula_info in listacines.get("peliculas").values():
            if generoteclado in pelicula_info["genero"]:
                titulos.append(pelicula_info["titulo"])
        print(','.join(titulos))
        tituloteclado = input("Introduce el título de la película: ")
        if tituloteclado not in titulos:
            print("Película no válida, saliendo.")
            return False
        else:
            for pelicula_info in listacines.get("peliculas").values():
                if tituloteclado == pelicula_info["titulo"]:
                    return pelicula_info["sipnosis"] 

def esperar_continuar():
    input("Presiona Enter para continuar...")
