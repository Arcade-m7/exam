from .api import DirEntry, FileEntry
from .api import scandir, join, isdir, getcwd, glob

def SORTBYNAME(Any: list[DirEntry|FileEntry]):
    Any.sort(
        key = lambda elem : elem.name
    )
    return Any

def SORTBYDATEMODIFIED(Any: list[FileEntry]):
    Any.sort(
        key = lambda elem : elem.Details.st_mtime if hasattr(elem.Details,'st_mtime') else elem.name
    )
    return Any

def SORTBYEXTENSSION(Any: list[FileEntry]):
    Any.sort(
        key = lambda elem : elem.extension if hasattr(elem,'extension') else elem.name
    )
    return Any

def SORTBYSIZE(Any: list[FileEntry|DirEntry]):
    Any.sort(
        key = lambda elem : elem.Details.st_size
    )
    return Any

def SORTBYDATECREATED(Any: list[FileEntry|DirEntry]):
    Any.sort(
        key = lambda elem : elem.Details.st_ctime
    )
    return Any

def DONTSORT(Any:list[FileEntry,DirEntry]):
    return Any

def Search(pwd: str = getcwd(), pattern: str = '*',error: bool = False):
    assert isdir(pwd), 'pwd must be a directory'
    Path = [pwd]
    while (path:= Path.pop(0) if len(Path) != 0 else None):
        try:
            for searchResult in glob(pattern, root_dir=path):
                yield join(path,searchResult)
            for element in scandir(path):
                if element.is_dir():
                    Path.append(element.path)
        except Exception as e:
            print(f'Error while searching in {path} : {e}') if error else None
            continue