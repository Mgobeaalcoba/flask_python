from flask import render_template, session, flash, redirect, url_for

from app.forms import LoginForm
from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }

    # Si mi route acepta request post entonces puedo usar esos datos.
    if login_form.validate_on_submit():
        username = login_form.username.data # Todo el username del post para guardarlo en la sesion
        session['username'] = username # Guardo el username en mi sessión para luego usarlo en el "GET"

        # Guardo un flash en memoría que luego debo reenderiarlo en HTML:
        flash('Nombre de usuario registrado con exito!')

        # Redirijo a index en caso de que completen el form:
        return redirect(url_for('index'))

    return render_template('login.html', **context)