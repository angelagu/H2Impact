from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('intro.html')


@app.route('/account')
def account():
    return render_template('bootstrap_index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/mysage')
def my_sage():
    return render_template('my_sage.html')


if __name__ == '__main__':
    app.run(debug=True)
