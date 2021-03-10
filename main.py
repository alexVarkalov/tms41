from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
db = SQLAlchemy(app)


class Group(db.Model):
    __tablename__ = 'group'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(255))


db.init_app(app)
db.create_all()


@app.route('/')
def groups():
    groups = Group.query.all()
    return render_template('groups.html', groups=groups)


@app.route('/create_group', methods=['GET', 'POST'])
def create_group():
    if request.method == 'GET':
        return render_template('create_group.html')
    else:
        fullname = request.form['fullname']
        group = Group(fullname=fullname)
        db.session.add(group)
        db.session.commit()
        return redirect(url_for('groups'))


@app.route('/edit_group/<int:group_id>', methods=['GET', 'POST'])
def edit_group(group_id):
    group = Group.query.filter_by(id=group_id).one()
    if request.method == 'GET':
        return render_template('edit_group.html', group=group)
    else:
        fullname = request.form['fullname']
        group.fullname = fullname
        db.session.add(group)
        db.session.commit()
        return redirect(url_for('groups'))


@app.route('/delete_group/<int:group_id>', methods=['POST'])
def delete_group(group_id):
    group = Group.query.filter_by(id=group_id).one()
    db.session.delete(group)
    db.session.commit()
    return redirect(url_for('groups'))
