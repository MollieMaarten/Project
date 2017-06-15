from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/licht')
def licht():
    return render_template('licht.html')

@app.route('/temperatuur')
def temp():
    return render_template('temp.html')

@app.route('/vochtigheid')
def vocht():
    return render_template('vocht.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()
