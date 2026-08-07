from flask import current_app as app
from flask import render_template


from flask import render_template

@app.route("/")
@app.route("/login/")
def signin():
    return render_template("login.html")

@app.route("/admin")
def admin_dashboard():
    return render_template("patient_details.html", app_data=app_dct)

app_dct = [
    {"dname": "abc", "pname": "xyz", "spz": "Neurology"},
    {"dname": "pqr", "pname": "stu", "spz": "Cardiology"},
]
