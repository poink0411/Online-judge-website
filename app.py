from flask import *
from functions.correction import *
from functions.login import *
from functions.register import *
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/test', methods=['POST', 'GET'])
def test():
    if request.method=="POST":
        id="21053"
        prob_number="1001"
        with open('./data/'+id+'/ans_code_'+prob_number+'.py', 'w', encoding='utf-8') as f:
            f.write(request.form['codes'])
        if check_correct(0, 0):
            return "맞았습니다!"
        else:
            return "틀렸습니다!"
    return render_template('test.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method=="POST":
        if valid_login(request.form['id'], request.form['pw']):
            with open('./data/user_info.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
            return redirect(url_for('mainpage', username=data[request.form['id']]['username']))
        else:
            return render_template('login.html', error='아이디와 비밀번호를 다시 입력해주세요')
    return render_template('login.html', error=None)

@app.route('/admin/register', methods=['POST', 'GET'])
def register():
    if request.method=='POST':
        if request.form['new_year'] != "":
            register_year(int(request.form['new_year']))
        if request.form['past_year'] != "":
            delete_year(int(request.form['past_year']))
        return "등록: {}\n삭제: {}".format(request.form['new_year'], request.form['past_year'])
    return render_template('register.html')


@app.route('/main/<username>', methods=['POST', 'GET'])
def mainpage(username):
    return username+" 반갑습니다!"

@app.route('/main/<username>/mypage')
def mypage(username):
    return render_template('mypage.html')

if __name__ == '__main__':
    app.run()
