from os import listdir
from os.path import isfile, join

def return_contents():
    onlyfiles = [f for f in listdir() if isfile(f)]
    onlydirs = [f for f in listdir() if not isfile( f)]

    return(onlydirs,onlyfiles)

path = ""

def walk_path(folder):
    global path
    try:
        onlyfiles = [f for f in listdir(path+folder) if isfile(join(path+folder,f))]
        onlydirs = [f for f in listdir(path+folder) if not isfile(join(path+folder,f))]
        path = path+folder+"/"
        return(onlydirs,onlyfiles)

    except exception as e:
        return(["Path invalid"]["Please refresh"])
