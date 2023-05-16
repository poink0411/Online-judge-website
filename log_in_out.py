from flask import *
from functions.login import *
from app import session

log_in_out = Blueprint('log_in_out', __name__, url_prefix='/')
@log_in_out.route('/login', methods=['POST', 'GET'])
def login():
    if request.method=="POST":
        if valid_login(request.form['id'], request.form['pw']):
            with open('./data/user_info.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
            session['logged_in'] = True
            session['id'] = request.form['id']
            return redirect(url_for('mainpage.index'))
        else:
            return render_template('login.html', error='아이디와 비밀번호를 다시 입력해주세요')
    return render_template('login.html', error=None)

@log_in_out.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('id', None)
    return "로그아웃됨"
