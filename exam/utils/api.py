from os.path import isfile, isdir, join
from os import stat, getcwd, scandir
from glob import glob

class Base:
    
    def __init__(self,path: str,*args: tuple, **keys: dict):
        self.Details = stat(*args,**keys)
        self.path = path
        self.sep = '/'.join(
            list(
                filter(
                    lambda x : x,
                    self.path.split('\\')
                )
            )
        )
        self.name = self.sep.split('/')[-1]

class FileEntry(Base):

    def __init__(self, path: str):
        if not isfile(path):
            raise ValueError('path must be a file')
        self.extension = self.name.split('.')[-1] if '.' in self.name else None
        super().__init__(path)

    def __repr__(self):
        return self.name

class DirEntry(Base):

    def __init__(self, path: str):
        if not isdir(path):
            raise ValueError('path must be a dir')
        super().__init__(path)

    def __repr__(self):
        return self.name

class PathEntry:

    def __init__(self,pwd: str = getcwd()):
        self.Files = [] ; self.Dirs = []
        for element in scandir(pwd):
            if element.is_dir():
                self.Dirs.append(
                    DirEntry(
                        element.path
                    )
                )
            else:
                self.Files.append(
                    FileEntry(
                        element.path
                    )
                )
        self.Both = self.Files + self.Dirs

    def __repr__(self):
        return str(self.Both)