from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField
from wtforms.fields import EmailField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length


class MakeUserForm(FlaskForm):
    email = EmailField('Почта пользователя', validators=[DataRequired("Пожалуйста, введите вашу почту")])
    name = StringField('Имя пользователя', validators=[Length(min=0, max=32), DataRequired()])
    last_name = StringField('Фамилия пользователя', validators=[Length(min=0, max=32)])
    patronymic = StringField('Отчество пользователя', validators=[Length(min=0, max=32)])
    teacher = BooleanField('Пользователь является учителем?')
    about = TextAreaField("О себе", validators=[
        Length(min=0, max=512, message="Описание должно быть короче 512 символов")])
    submit = SubmitField('Создать')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Старый пароль', validators=[Length(min=6, max=32), DataRequired()])
    password = PasswordField('Новый пароль', validators=[Length(min=6, max=32), DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[Length(min=6, max=32), DataRequired()])
    submit = SubmitField('Сохранить')


class ChangeDataForm(FlaskForm):
    email = EmailField('Почта пользователя', validators=[DataRequired("Пожалуйста, введите вашу почту")])
    name = StringField('Введите имя', validators=[Length(min=0, max=32), DataRequired()])
    last_name = StringField('Введите фамилию', validators=[Length(min=0, max=32)])
    patronymic = StringField('Введите отчество', validators=[Length(min=0, max=32)])
    about = TextAreaField("О себе", validators=[
        Length(min=0, max=512, message="Описание должно быть короче 512 символов")])
    submit = SubmitField('Сохранить')


class ChangeProfileForm(FlaskForm):
    name = StringField('Введите имя', validators=[Length(min=0, max=32), DataRequired()])
    last_name = StringField('Введите фамилию', validators=[Length(min=0, max=32)])
    patronymic = StringField('Введите отчество', validators=[Length(min=0, max=32)])
    about = TextAreaField("О себе", validators=[
        Length(min=0, max=512, message="Описание должно быть короче 512 символов")])
    password = PasswordField('Новый пароль', validators=[Length(min=6, max=32), DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[Length(min=6, max=32), DataRequired()])
    submit = SubmitField('Сохранить')


class ChangeAuthorisedProfileForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired("Пожалуйста, введите вашу почту")])
    name = StringField('Введите имя', validators=[Length(min=0, max=32), DataRequired()])
    last_name = StringField('Введите фамилию', validators=[Length(min=0, max=32)])
    patronymic = StringField('Введите отчество', validators=[Length(min=0, max=32)])
    about = TextAreaField("О себе", validators=[
        Length(min=0, max=512, message="Описание должно быть короче 512 символов")])
    old_password = PasswordField('Старый пароль', validators=[Length(min=6, max=32), DataRequired()])
    password = PasswordField('Новый пароль', validators=[Length(min=6, max=32), DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[Length(min=6, max=32), DataRequired()])
    submit = SubmitField('Сохранить')


class MakePasswordForm(FlaskForm):
    password = PasswordField('Пароль', validators=[Length(min=6, max=32), DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[Length(min=6, max=32), DataRequired()])
    submit = SubmitField('Сохранить пароль')
    

class ForgotPasswordForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired("Пожалуйста, введите вашу почту")])
    submit = SubmitField('Отправить письмо')


class LoginForm(FlaskForm):
    email = EmailField('Введите почту', validators=[DataRequired()])
    password = PasswordField('Введите пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
