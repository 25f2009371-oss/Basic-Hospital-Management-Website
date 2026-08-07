from flask import Flask,render_template

app=Flask(__name__)



@app.route("/login")
def signin():
    return render_template("login.html")

app_dct=[{"dname":"abc","pname":"xyz","spz":"Neurology"},
         {"dname":"pqr","pname":"stu","spz":"Cardiology"},
         {"dname":"qqpqqceqr","pname":"qeq","spz":"Nephrology"},
         {"dname":"eqqr","pname":"stu","spz":"Dentist"}
    ]


@app.route("/admin")
def admin_console():
    return render_template("admin_dashboard.html",app_data=app_dct)

if __name__=="__main__":
    app.run(debug=True)