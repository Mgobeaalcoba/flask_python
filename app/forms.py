from flask_wtf import FlaskForm 
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

# Class LoginForm que hereda de FlaskForm:
class LoginForm(FlaskForm):
    # Los forms tienen campos o field que deben llenarse:
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()]) # WTF va a manejar pertinentemente estos password. Es decir de forma segura.
    # Agregamos un validador de datos que también lo tiene WTF
    # Agregamos un SubmitField como botón de envio:
    submit = SubmitField("Enviar")

# Class LoginForm que hereda de FlaskForm:
class SignupForm(FlaskForm):
    # Los forms tienen campos o field que deben llenarse:
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()]) # WTF va a manejar pertinentemente estos password. Es decir de forma segura.
    repeat_password = PasswordField('Repetir password', validators=[DataRequired()])
    # Agregamos un validador de datos que también lo tiene WTF
    # Agregamos un SubmitField como botón de envio:
    submit = SubmitField("Enviar")

# Class TodoForm que hereda de FlaskForm y se usará para cargar tareas: 
class TodoForm(FlaskForm):
    description = StringField('Descripción', validators=[DataRequired()])
    submit = SubmitField('Crear')

# Class DeleteForm que hereda de FlaskForm y se usará para eliminar tareas:
class DeleteTodoForm(FlaskForm):
    submit = SubmitField('Eliminar')