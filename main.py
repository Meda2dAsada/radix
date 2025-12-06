#import sys
#sys.setrecursionlimit(n)
from src.components.radix import Radix
from src.classes.directory import Directory
from src.classes.json_reader import JsonReader
from src.classes.file import File
from src.classes.entry_creator import EntryCreator

#TODO: add dynamic configuration system to all components with JsonReader class
#TODO: fix issues with the hashing of the unhashable type: 'EntryScreen'
#TODO: add themes for app
Radix().run()