from flask import Flask, render_template
import read
app = Flask(__name__)


@app.route('/')
def do_search() -> str:
    quits = str(read.r_column(0, 'x.xlsx'))
    return render_template('results.html', the_paragraph=quits)


if __name__ == '__main__':
    app.run(debug=True)
