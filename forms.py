from wtforms import Form
from wtforms import StringField, PasswordField, EmailField, BooleanField, SubmitField, IntegerField, DateField, RadioField
from wtforms import validators
from wtforms.validators import DataRequired
from datetime import datetime


class UserForm(Form):
    matricula = IntegerField("Matricula",[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=3,max=10,message='De 3 - 10 caracteres')
    ])
    nombre = StringField("Nombre",[
        validators.DataRequired(message='El campo es requerido')
        ])
    apellido = StringField("Apellido",[
        validators.DataRequired(message='El campo es requerido')
        ])
    correo = EmailField("Correo",[
        validators.DataRequired(message='El correo es requerido')
        ])
