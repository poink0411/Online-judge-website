from flask import *
from datetime import timedelta
from functions.register import *
from log_in_out import *
from mainpage import *
app = Flask(__name__)
app.secret_key="sadlfksadfljkaew"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=2)
app.register_blueprint(log_in_out)
app.register_blueprint(mainpage)
@app.route('/admin/register', methods=['POST', 'GET'])
def register():
    if request.method=='POST':
        if request.form['new_year'] != "":
            register_year(int(request.form['new_year']))
        if request.form['past_year'] != "":
            delete_year(int(request.form['past_year']))
        return "등록: {}\n삭제: {}".format(request.form['new_year'], request.form['past_year'])
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)