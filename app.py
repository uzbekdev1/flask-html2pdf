from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'HTML to PDF Flask Api!'


@app.route('/html/<int:size>.pdf')
def html(size):
    cols = 4
    return render_template('test.html', headers=range(0, round(size / cols)), footers=range(0, size % cols),
                           cells=range(0, cols))


if __name__ == "__main__":
    app.run()
