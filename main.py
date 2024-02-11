from flask import Flask, render_template, redirect

from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    params = {'title': 'Список профессий', 'list_type': list_type,
              'profs': ['механик', 'инженер', 'я', 'биолог']}
    return render_template('professions_list.html', **params)


@app.route('/training/<prof>')
def training(prof):
    params = {
        'title': prof,
        'engineer': True if 'инженер' in prof or "строитель" in prof else False
    }
    return render_template('training.html', **params)


@app.route('/answer')
@app.route('/auto_answer')
def answers():
    params = {'title': 'Анкета',
              'surname': 'Иванов',
              'name': 'Иван',
              'education': 'Высшее Ивановское',
              'profession': 'Трубадур',
              'sex': 'Ламинат',
              'motivation': 'Первый трубадур на марсе',
              'ready': 'True'}
    return render_template('auto_answer.html', **params)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)


@app.route('/distribution')
def distribution():
    params = {'title': 'Каюты', 'astronauts': ['Я', 'Маша', 'Миша', 'Катя']}
    return render_template('distribution.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
