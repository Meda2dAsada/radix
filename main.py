#import sys
#sys.setrecursionlimit(n)
from src.components.radix import Radix
from src.classes.directory import Directory
from src.classes.json_reader import JsonReader
from src.classes.file import File
from src.classes.entry_creator import EntryCreator


# # Crear directorio raíz
# folder = Directory('folder', r'C:\Users\ASADA\Desktop\py_projects\protor')

# files = [File(f'file{i}.txt', content=f'Contenido del archivo {i}') for i in range(1, 6)]

# r = r'C:\Users\ASADA\Desktop\py_projects\protor\json\constants.json'

#TODO: add dynamic configuration system to all components with JsonReader class
#TODO: fix issues with the hashing of the unhashable type: 'EntryScreen'
#TODO: add themes for app
Radix().run()