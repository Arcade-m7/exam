from src import PathEntry, algorithmes
from os import getcwd

class FileExplorer:

    def ls(pwd:str = getcwd(), Sort: algorithmes = algorithmes.DONTSORT):
        
        return 