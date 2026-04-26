from utils import PathEntry, SearchEntry, algorithmes
from os import getcwd,scandir

for searchresult in SearchEntry.Search('c:/','*.txt'):
    print(searchresult)