from flask import Flask
import subprocess

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Html to Pdf parser!"


@app.route('/html2pdf')
def html2pdf():
    subprocess.run("./wkhtmltopdf.exe http://localhost:5000/static/test.html ./static/test.pdf")
    return "done!"


if __name__ == '__main__':
    app.run()
