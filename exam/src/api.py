from os.path import isfile, isdir
from os import stat, getcwd, scandir
from dataclasses import dataclass

class Base:
    
    def __init__(self,*args,**keys):
        self.Details = stat(*args,**keys)

class FileEntry(Base):

    def __init__(self, path: str):
        if not isfile(path):
            raise ValueError('path must be a file')
        self.path = path
        sep = '/'.join(self.path.split('\\'))
        self.name = sep.split('/')[-1]
        self.extension = self.name.split('.')[-1] if '.' in self.name else None
        super().__init__(path)

    def __repr__(self):
        return self.name

class DirEntry(Base):

    def __init__(self, path: str):
        if not isdir(path):
            raise ValueError('path must be a dir')
        self.path = path
        sep = '/'.join(
            list(
                filter(
                    lambda x : x or '',
                    self.path.split('\\')
                )
            )
        )
        self.name = sep.split('/')[-1]
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

    def __repr__(self):
        return [elem.name for elem in self.Files + self.Dirs]