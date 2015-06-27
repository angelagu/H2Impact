import requests
import os
import json

from flask import Flask, Response, request, session, g, redirect, url_for, abort, render_template, flash
from urlparse import urljoin
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


class Shower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    shower_length = db.Column(db.Integer, index=True)
    time = db.Column(db.DateTime, index=True, server_default=db.func.now())

    def __repr__(self):
        return '<User %r>' % (self.name)


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


@app.route('/api/<path:path>', methods=['GET'])
def api(path):
    clientToken = ''
    clientSecret = ''
    baseUrl = 'https://suggestqueries.google.com'
    accessToken = ''

    # Authentication
    #
    # session.auth = EdgeGridAuth (
    #     client_token = clientToken,
    #     client_secret = clientSecret,
    #     access_token = accessToken
    # )

    r = requests.get(urljoin(baseUrl, path), params=request.args)

    if r.status_code != requests.codes.ok:
        return None

    return Response(r.content,  mimetype='application/json')

if __name__ == "__main__":
    app.run(debug=True)
