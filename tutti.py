# -*- coding: utf-8 -*-
"""
    Tutti

    A microblogging application written with Flask and sqlite3.

    :Copyright: (c) 2014 by Tutti.
"""

import time

from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash, _app_ctx_stack

# configuration
DATABASE = '/tmp/minitwit.db'
DEBUG = True
SECRET_KEY = 'development key'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    """Shows main page or if no user is logged in it will
    redirect to the normal main page.
    """
    """
    if not g.user:
        return redirect(url_for('logged_in_main'))
    """
    return render_template('main.html')


@app.route('/main')
def logged_in_main():
    """Displays the main page with user information."""
    return render_template('main.html')

@app.route('/about')
def about():
    """Displays the main page with user information."""
    return render_template('about.html')

@app.route('/repertory')
def repertory():
    """Displays the main page with user information."""
    return render_template('repertory.html')

@app.route('/request')
def request():
    """Displays the main page with user information."""
    return render_template('request.html')

@app.route('/musicians')
def musicians():
    """Displays the main page with user information."""
    return render_template('musicians.html')

@app.route('/people')
def people():
    """Displays the main page with user information."""
    return render_template('people.html')


@app.route('/contact')
def contact():
    """Displays the main page with user information."""
    return render_template('contact.html')

@app.route('/board')
def board():
    """Displays the main page with user information."""
    return render_template('board.html')



if __name__ == '__main__':
    #init_db()
    app.run(host='0.0.0.0', port=81)
