from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home():
    return 'Home page'


@app.route('/save_data', methods=['POST'])
def save_data():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    age = request.form['age']
    record = f'{firstname} - {lastname} - {age}\n'
    with open('flask_04.txt', 'a') as data_file:
        data_file.write(record)
    return 'Saved'


if __name__ == '__main__':
    app.run()
