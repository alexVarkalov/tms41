from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return 'Home page'


@app.route('/my_word/<string:word>')
def my_word(word):
    if len(word) % 2 == 0:
        return word[::2]
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
