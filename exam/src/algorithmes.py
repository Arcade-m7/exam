from .api import DirEntry, FileEntry

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