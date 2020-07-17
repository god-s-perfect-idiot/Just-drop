from flask import Flask, render_template, request, jsonify
import model
import service

app = Flask(__name__)

previous=""
dir=[]
file=[]

@app.route("/")
def home():
    global dir,file,previous
    previous=""
    dirs,files,current = service.getfiles()
    dir = dirs
    file = files
    return render_template('index.html', dirs=dirs, files=files, current=current)

@app.route("/req/<obj>")
def req(obj):
    global dir, file, previous
    if(obj in dir):
        dirs,files = service.traverse(obj)
        current = previous
        previous = "root/"
        dir = dirs
        file = files
        return render_template('index.html', dirs = dirs, files = files, current=current)
    elif(obj in file):
        print("caught")
        return render_template('index.html', dirs = dir, files = file, current=obj)


if(__name__=="__main__"):
    app.run(debug=True)
