from flask import Flask, request, render_template

app = Flask(__name__, template_folder='../templates')


@app.route('/')
def home():
    return 'Home page'


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('flask_06_form.html')
    else:
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        age = request.form['age']
        return render_template(
            'flask_06_display.html',
            firstname=firstname,
            lastname=lastname,
            age=age,
        )


if __name__ == '__main__':
    app.run()
