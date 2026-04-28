from src import PathEntry, algorithmes, Search
from os import getcwd,scandir
from time import time,sleep

def CountTimeToExecAFunction(func,*args,**keys):
    st = time() ; return func(*args,**keys), time() - st

icons = 'https://www.flaticon.com/packs/file-extension-4?word=files%20and%20folders'
"https://www.flaticon.com/packs/files-color/2"
"https://www.flaticon.com/packs/files-and-folders-25?word=files%20and%20folders"

