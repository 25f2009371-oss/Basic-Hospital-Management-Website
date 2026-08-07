#define all routes here 
from app import *


app_dct=[{"dname":"abc","pname":"xyz","spz":"Neurology"},
         {"dname":"pqr","pname":"stu","spz":"Cardiology"}
    ]


@app.route("/login/")
def signin():
    return render_template("login.html")


#data dictiona=


@app.route("/admin")
def admin_console():
    return render_template("admin_dashboard.html",appointments=app_dct)
