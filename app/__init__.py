import requests
import os
import json
from sqlalchemy.sql import func

from flask import Flask, Response, request, session, g, redirect, url_for, abort, render_template, flash
from flask import jsonify
from urlparse import urljoin
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('../config.py')
db = SQLAlchemy(app)


class Shower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True)
    shower_length = db.Column(db.Integer, index=True)
    time = db.Column(db.DateTime, index=True, server_default=db.func.now())

    def __repr__(self):
        return str(self.__dict__)

    def get_min(self, name):
        return


@app.route('/')
def index():
    return render_template('intro.html')


@app.route('/account')
def account():
    return render_template('bootstrap_index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/mysage/<username>', methods=['GET'])
def show_showers(username):
    shower_min = Shower.query.filter_by(name=username).order_by(Shower.shower_length).first().shower_length
    shower_max = Shower.query.filter_by(name=username).order_by(Shower.shower_length.desc()).first().shower_length
    average = db.session.query(func.avg(Shower.shower_length).label('average')).filter(Shower.name==username).first()[0]
    return render_template('my_sage.html', min=shower_min, max=shower_max,
                           average=average, name=username)

if __name__ == "__main__":
    app.run(debug=True)
