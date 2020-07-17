from flask import Flask, render_template, request, jsonify, send_file, send_from_directory, abort
import model
import service

file = []

app = Flask(__name__)

@app.route("/")
def home():
    global file

    files = service.getfiles()
    file = files
    return render_template('index.html', files=files)

@app.route("/req/<obj>")
def req(obj):
    if(obj in file):
        print("caught")
        return send_file(obj, as_attachment=True)
    else:
        print("erred")
        abort(404)

@app.route("/upload", methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        file = request.files
        print(s)

    return render_template('index.html', files=file)

if(__name__=="__main__"):
    app.run(host="0.0.0.0", debug=True)
