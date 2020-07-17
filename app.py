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


if(__name__=="__main__"):
    app.run(debug=True)
