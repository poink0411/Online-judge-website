from flask import *
from functions.register import *
from app import session
import os
admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/register/user', methods=['POST', 'GET'])
def register_user():
    if session['id'] != "0":
        return redirect(url_for('log_in_out.login'))
    if request.method == 'POST':
        if request.form['new_year'] != "":
            register_year(int(request.form['new_year']))
        if request.form['past_year'] != "":
            delete_year(int(request.form['past_year']))
        return "등록: {}\n삭제: {}".format(request.form['new_year'], request.form['past_year'])
    return render_template('register_user.html')

@admin.route('/register/problem', methods=['POST', 'GET'])
def register_problem():
    if session['id'] != "0":
        return redirect(url_for('log_in_out.login'))
    if request.method == 'POST':
        if request.form['prob_num'] not in os.listdir('./problems'):
            os.mkdir('./problems/'+str(request.form['prob_num']))
        path = './problems/'+str(request.form['prob_num'])
        with open(path+'/test_case.txt', 'w') as test_case:
            test_case.write(request.form['test_case'])
        with open(path+'/test_case_ans.txt', 'w') as test_case_ans:
            test_case_ans.write(request.form['test_case_ans'])
        with open(path+'/text.txt', 'w') as text:
            text.write(request.form['text'])
        return render_template('register_problem.html')
    return render_template('register_problem.html')
