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

def listar(a):
    if current_path.is_dir():
        for dir in current_path.iterdir():
            if dir.is_file and dir.suffix == '.txt':
                print(dir.name)
            
def leer(b):
    file_path = current_directory / str(nombre)
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)

def eliminar(c):
    path_origen.unlink()
    print("Se ha eliminado el archivo")


print("""Seleccione una opción:  
        1) Listar los documentos de texto de esta carpeta  
        2) Leer un documento  
        3) Eliminar un documento
        4) Salir del programa""")

opcion = input('Opción: ')

if opcion == '1':
    clearConsole()
    print('Estos son los documentos de texto en esta carpeta:')
    listar(input)
    print('Presione x para regresar al menú')

elif opcion == '2':
    clearConsole()
    nombre = input('¿Cuál es el nombre del texto que te gustaría leer? ')
    leer(nombre)
    print('Presione x para regresar al menú')

elif opcion == '3':
    clearConsole() 
    origen = input('¿Cuál es el nombre del texto que le gustaría eliminar? ')
    path_origen = current_path / origen
    eliminar(path_origen)
    print('Presione x para regresar al menú')


