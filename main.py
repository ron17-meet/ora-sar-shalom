#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory, session as login_session, g
app = Flask(__name__)
app.secret_key = 'wae70712490124n_eqdwea'

@app.route('/', methods=["GET", "POST"])
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug = True)