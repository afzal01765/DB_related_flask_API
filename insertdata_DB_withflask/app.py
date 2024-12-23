from MySQLdb.cursors import Cursor
from  flask import  Flask , render_template, request, session , redirect, url_for ,sessions
from  flask_mysqldb import  MySQL
import  MySQLdb.cursors
import  re

app = Flask(__name__)
app.secret_key = 'xyz123#$'
app.config["MYSQL_HOST"] ='localhost'
app.config["MYSQL_USER"] ='root'
app.config["MYSQL_DB"] = 'user_system'

mysql = MySQL(app)

@app.route("/")
@app.route("login",methods =["GET","POST"])

def login():

    massage = ''
    if request.method =="POST" and 'email' in request.form and 'password' in request.form:
        email = request.form["email"]
        password =request.form["password"]
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("select from where email =%s and password =%s",(email,password))
        user = cursor.fetchone()
        if user:
            session["loggedin"] = True
            session["userid"] = user["userid"]
            session["name"]  = user["name"]
            session["email"] = user["email"]
            massage = "logged in successfully"
            return render_template(url_for("user.html",massage = massage))
        else:
            massage = "Please Enter currect Email / password"
    return render_template(url_for("login.html",massage = massage ))

@app.route("/logout")
def logout():
    session["user"]
if __name__ =="__main__":
    app.run()


