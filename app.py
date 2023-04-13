import flask
import flask_wtf
import wtforms
import json


class RegisterForm(flask_wtf.FlaskForm):
    log_in = wtforms.StringField('Log in')
    email = wtforms.EmailField('Email')
    password = wtforms.PasswordField('Password')
    submit = wtforms.SubmitField('Register!')


app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'Aa'


@app.route('/')
def index():  # put application's code here
    return 'Hello World!'


@app.route('/registration/', methods=['GET', 'POST'])
def register_view():
    form = RegisterForm()
    if flask.request.method == 'GET':
        return flask.render_template('registration.html', form=form)

    l_data = form.log_in.data
    e_data = form.email.data
    p_data = form.password.data

    user_data = [{'login': form.log_in.data,
                  'email': form.email.data,
                  'password': form.password.data}]

    with open('user_data.json', 'w') as file:
        json.dump(user_data, file, ensure_ascii=False)

    return f"login: {l_data} email: {e_data} password: {p_data}"


if __name__ == '__main__':
    app.run(debug=True)
