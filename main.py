from flask import Flask, render_template

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
    param = {
        'title': prof
    }
    param[
        'engineer'] = True if 'инженер' in prof or "строитель" in prof else False
    return render_template('training.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
