from pathlib import Path
import shutil
from turtle import clear
import keyboard
import os

current_directory = Path.cwd()
current_path = Path(current_directory)

def clearConsole():
    command = 'cls'
    os.system(command)

def listar():
    if current_path.is_dir():
        for dir in current_path.iterdir():
            if dir.is_file and dir.suffix == '.txt':
                print(dir.name)
            
def leer(nombre):
    file_path = current_directory / str(nombre)
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)

def eliminar(path_origen):
    path_origen.unlink()
    print("Se ha eliminado el archivo")

def crear(nombre_archivo):
    file_path = current_directory / str(nombre_archivo)
    with open(file_path, 'w') as file:
        file.write(texto)

def inicio():
    print("""Seleccione una opción:  
        1) Listar los documentos de texto de esta carpeta  
        2) Leer un documento  
        3) Eliminar un documento
        4) Crear un documento
        5) Salir del programa""")

while True:
    clearConsole()
    inicio()
    opcion = input('Opción: ')

    while opcion == '1':
        archivos = ''
        clearConsole()
        print('Estos son los documentos de texto en esta carpeta:')
        listar()
        salir = input('Ingrese x para regresar al menú: ')
        if salir == 'x':
            break

    while opcion == '2':
        clearConsole()
        nombre = input('¿Cuál es el nombre del texto que te gustaría leer? ')
        leer(nombre)
        salir = input('Ingrese x para regresar al menú: ')
        if salir == 'x':
            break

    while opcion == '3':
        clearConsole() 
        origen = input('¿Cuál es el nombre del texto que le gustaría eliminar? ')
        path_origen = current_path / origen
        eliminar(path_origen)
        salir = input('Ingrese x para regresar al menú: ')
        if salir == 'x':
            break

    while opcion == '4':
        clearConsole()
        nombre_archivo = input("Nombre del archivo: ")
        texto = input("Escribe algo en el archivo: ")
        crear(nombre_archivo)
        print("El archivo se ha creado")
        salir = input('Ingrese x para regresar al menú: ')
        if salir == 'x':
            break

    if opcion == '5':
        break
