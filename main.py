from flask import Flask, url_for

app = Flask(__name__)
promo_list = ('Человечество вырастает из детства.',
              '',
              '',
              '', 'Присоединяйся!')


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def promotion_image(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    
                    crossorigin="anonymous">
                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                      <h2>Прентендент на участие в миссии:{nickname}</h2>
                    <div class="alert alert-success" role="alert">
                      Поздравляем! Ваш рейтинг после {str(level)} этапа отбора
                    </div>
                    <p>составляет {str(rating)} баллов!</p>
                    <div class="alert alert-warning" role="alert">
                      Желаю удачи;
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
