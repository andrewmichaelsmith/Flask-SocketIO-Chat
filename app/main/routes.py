from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import LoginForm

import os
import random

names_file = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '../../names.txt'
)

names = None

with open(names_file, 'r') as f:
    names = f.read().splitlines()

#@main.route('/', methods=['GET', 'POST'])
#def index():
#    """"Login form to enter a room."""
#    form = LoginForm()
#    if form.validate_on_submit():
#        session['name'] = form.name.data
#        session['room'] = form.room.data
#        return redirect(url_for('.chat'))
#    elif request.method == 'GET':
#        form.name.data = session.get('name', '')
#        form.room.data = session.get('room', '')
#    return render_template('index.html', form=form)
#

@main.route('/', methods=['GET', 'POST'])
def index():
    if 'name' not in session:
        session['name'] = random.choice(names)
    if 'room' not in session:
        session['room'] = ''


    return render_template(
     'chat.html', name=session['name'], room=session['room']
    )
