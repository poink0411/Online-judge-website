from flask import *
from app import session
from functions.correction import *
import os
mainpage = Blueprint('mainpage', __name__, url_prefix='/')

@mainpage.route('/index', methods=['POST', 'GET'])
def index():
    if 'logged_in' not in session:
        return redirect(url_for('log_in_out.login'))
    if request.method=="POST":
        return redirect(url_for('mainpage.viewprob', prob_num=request.form['p_num']))
    return render_template('index.html', problems=os.listdir('./problems'))

@mainpage.route('/index/<prob_num>', methods=['POST', 'GET'])
def viewprob(prob_num):
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    if request.method=="POST":
        id = session['id']
        with open('./data/' + id + '/ans_code_' + prob_num + '.py', 'w', encoding='utf-8') as f:
            f.write(request.form['codes'])
        if check_correct(prob_num, id):
            return "맞았습니다!"
        else:
            return "틀렸습니다!"
    with open('./problems/'+str(prob_num)+'/text.txt', 'r', encoding='utf-8') as file:
        return render_template('viewprob.html', problem_num=prob_num, problem_text=file.read())