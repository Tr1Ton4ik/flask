import json

from flask import Flask, render_template, redirect

from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=2)


@app.route('/news')
def news():
    with open("news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html', news=news_list)


@app.route('/queue')
def queue():
    return render_template('loop.html', title='abcdefg')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


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
