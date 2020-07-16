from flask import Flask, render_template, request, jsonify
import model
import service


app = Flask(__name__)

@app.route("/")
def home():
    dirs,files,current = service.getfiles()
    return render_template('index.html', dirs=dirs, files=files, current=current)

if(__name__=="__main__"):
    app.run(debug=True)
