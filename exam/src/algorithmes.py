from api import DirEntry, FileEntry, PathEntry

def SORTBYNAME(Any: list[DirEntry|FileEntry]):
    Any.sort(
        key = lambda elem : elem.name
    )
    return Any

def SORTBYDATEMODIFIED(Any: list[FileEntry]):
    Any.sort(
        key = lambda elem : elem.Details.st_mtime
    )
    return Any

def SORTBYEXTENSSION(Any: list[FileEntry]):
    Any.sort(
        key = lambda elem : elem.extension
    )
    return Any

def SORTBYSIZE(Any: list[FileEntry]):
    Any.sort(
        key = lambda elem : elem.Details.st_size
    )
    return Any

def SORTBYEXTENSSION(Any: list[FileEntry|DirEntry]):
    Any.sort(
        key = lambda elem : elem.Details.st_ctime
    )
    return Any