import model

def getfiles():
    files = model.return_contents()
    tmp=[]
    tmp.append(len(files))
    tmp.extend(files)
    files=tmp[:]
    return (files)
