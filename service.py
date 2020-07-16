import model

def getfiles():
    dirs, files = model.return_contents()
    tmp = []
    tmp.append(len(dirs))
    tmp.extend(dirs)
    dirs=tmp[:]
    tmp=[]
    tmp.append(len(files))
    tmp.extend(files)
    files=tmp[:]
    current = "root/"
    return (dirs, files, current)

def traverse(folder):
    dirs, files = model.walk_path(folder)
    return (dirs, files)
