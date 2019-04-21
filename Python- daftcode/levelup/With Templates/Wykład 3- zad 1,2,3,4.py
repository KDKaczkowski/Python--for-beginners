'''
2. Wykonaj endpoint:
'/login' - POST

na którym to możemy zalogować się do konta za pomocą poniższych sekretów:
login: TRAIN
pass: TuN3L

Po udanym logowaniu zostajemy przekierowani na endpoint '/hello'.
Autoryzacji dokonujemy poprzez BasicAuth.

Logowanie powinno umożliwić korzystanie z endpointów stworzonych w kolejnych
etapach. Podpowiadamy, trzeba utworzyć sesję, można samemu obsłużyć cookie,
albo skorzystać z gotowego mechanizmu: flask.session.

3.Kolejny endpoint '/logout' powinien:
- obsługiwać metodę POST
- być dostępny tylko dla zalogowanych użytkowników.
- gdy użytkownik nie jest zalogowany to przekieruj na '/login'

Po wykonaniu akcji, użytkownik powinien stracić możliwość korzystania z
chronionych endpointów ('/trains', '/logout', ...) i zostać przekierowany na
'/'.
4. Kolejny endpoint '/hello' powienien:
- obsługiwać metodę GET
- być dostępny tylko dla zalogowanych użytkowników
- przekierowywać na '/login' gdy użytkownik nie jest zalogowany
- zwracać pooprawny HTML z powitaniem

Poprawny dokument HTML powinien zawierać dowolny element (np. <p>, <h1>) z
atrybutem 'id=greeting'. Tekst powitania powinien być taki:
'Hello, {{ user }}!'.

Za '{{ user }}' wstawiamy nazwę użytkownika | użyj silnika templatek np.
jinja2.

'''


from flask import Flask, redirect, abort, request, session, render_template
from jinja2 import Environment, FileSystemLoader
 
env = Environment(loader=FileSystemLoader('templates'))
app = Flask(__name__)
app.secret_key = "secret key"
 
 
@app.route('/')
def hi():
    return 'hi'
 
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if 'log' in session:
        if session.get('log') == True:
            template = env.get_template('index.html')
            return template.render(user=session['username'])
        return redirect('/login')
    return redirect('/login')
 
 
 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.authorization and request.authorization.username == 'TRAIN' and request.authorization.password == 'TuN3L':
        session['log'] = True
        session['username'] = request.authorization.username
        return redirect('/hello')
    else:
        return abort(401)
 
@app.route('/logout',methods=['GET', 'POST'])
def logout():
    if 'log' in session:
        if session.get('log') == True:
            session['log'] = False
            return redirect('/')
    return redirect('/login')
 
#
if __name__ == '__main__':
    app.run(debug=False)