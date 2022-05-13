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

class Program: 
    def menu(self):
        print("""Seleccione una opción:  
            1) Listar los documentos de texto de esta carpeta  
            2) Leer un documento  
            3) Eliminar un documento
            4) Crear un documento
            5) Salir del programa""")

    def list_doc(self):
        if current_path.is_dir():
            for dir in current_path.iterdir():
                if dir.is_file and dir.suffix == '.txt':
                    print(dir.name)
            
    def read(self, name):
        file_path = current_directory / str(name)
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)

    def delete(self, path_origen):
        path_origen.unlink()
        print("Se ha eliminado el archivo")

    def create(self, file_name):
        file_path = current_directory / str(file_name)
        with open(file_path, 'w') as file:
            file.write(text)

program = Program()

while True:
    clearConsole()
    program.menu()
    option = input('Opción: ')

    while option == '1':
        archivos = ''
        clearConsole()
        print('Estos son los documentos de texto en esta carpeta:')
        program.list_doc()
        exit = input('Ingrese x para regresar al menú: ')
        if exit == 'x':
            break

    while option == '2':
        clearConsole()
        name = input('¿Cuál es el nombre del texto que te gustaría leer? ')
        program.read(name)
        exit = input('Ingrese x para regresar al menú: ')
        if exit == 'x':
            break

    while option == '3':
        clearConsole() 
        origin = input('¿Cuál es el nombre del texto que le gustaría eliminar? ')
        path_origin = current_path / origin
        program.delete(path_origin)
        exit = input('Ingrese x para regresar al menú: ')
        if exit == 'x':
            break

    while option == '4':
        clearConsole()
        file_name = input("Nombre del archivo: ")
        text = input("Escribe algo en el archivo: ")
        program.create(file_name)
        print("El archivo se ha creado")
        exit = input('Ingrese x para regresar al menú: ')
        if exit == 'x':
            break

    if option == '5':
        break
