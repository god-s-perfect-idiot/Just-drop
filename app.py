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
    global file

    if(obj in file):
        return send_file("root/"+obj, as_attachment=True)
    else:
        abort(404)

@app.route("/upload", methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save("root/"+f.filename)
        print("worked")
    files = service.getfiles()
    return render_template('index.html', files=files)

if(__name__=="__main__"):
    app.run(host="0.0.0.0", debug=True)
