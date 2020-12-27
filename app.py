from flask import Flask, render_template, send_file, request
import pdfkit, uuid

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/html/<int:size>')
def generate_html(size):
    cols = 4
    return render_template('widget.html', headers=range(0, round(size / cols)), footers=range(0, size % cols),
                           cells=range(0, cols))


@app.route('/pdf/<int:size>')
def generate_pdf(size):
    url = request.host_url + "html/" + str(size)
    name = str(uuid.uuid4()) + ".pdf"
    file = "static/tmp/" + name
    pdfkit.from_url(url, file)

    return send_file(file, attachment_filename=name)


if __name__ == "__main__":
    app.run(debug=True)
