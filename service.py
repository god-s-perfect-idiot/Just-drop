import model

def getfiles():
    dirs, files = model.return_contents
    return (dirs, files)

def traverse(folder):
    dirs, files = model.walk_path(folder)
    return (dirs, files)
