from os import listdir
from os.path import isfile, join

def return_contents():
    onlyfiles = [f for f in listdir() if isfile(f)]
    onlydirs = [f for f in listdir() if not isfile( f)]

    return(onlydirs,onlyfiles)

def walk_path(folder):
    try:
        onlyfiles = [f for f in listdir(folder) if isfile(join(folder,f))]
        onlydirs = [f for f in listdir(folder) if not isfile(join(folder,f))]
        return(onlydirs,onlyfiles)

    except exception as e:
        return(["Path invalid"]["Please refresh"])
