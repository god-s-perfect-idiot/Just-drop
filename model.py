from os import listdir
from os.path import isfile, join

def return_contents():
    onlyfiles = [f for f in listdir() if isfile(f)]
    return(onlyfiles)
