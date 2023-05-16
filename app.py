from flask import *
from datetime import timedelta
from functions.register import *
from log_in_out import *
from mainpage import *
from admin import *
app = Flask(__name__)
app.secret_key="sadlfksadfljkaew"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=2)
app.register_blueprint(log_in_out)
app.register_blueprint(mainpage)
app.register_blueprint(admin)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')