from flask import Flask, request, render_template

app = Flask(__name__, template_folder='../templates')


@app.route('/')
def home():
    return 'Home page'


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('flask_05.html')
    else:
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        age = request.form['age']
        record = f'{firstname} - {lastname} - {age}\n'
        with open('flask_05.txt', 'a') as data_file:
            data_file.write(record)
        return 'Saved'


if __name__ == '__main__':
    app.run()
