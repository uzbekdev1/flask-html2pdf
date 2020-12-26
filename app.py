from flask import Flask, jsonify
from flask_swagger import swagger
import subprocess

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Html to Pdf parser!"


@app.route('/html2pdf')
def html2pdf():
    subprocess.run("./wkhtmltopdf.exe http://localhost:5000/static/test.html ./static/test.pdf")
    return "done!"


@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Html to Pdf API"
    return jsonify(swag)

if __name__ == '__main__':
    app.run()
