from flask import Flask, render_template, request, url_for, redirect, flash, session, app
from dbconnection import connection
import MySQLdb
import gc
#from passlib.hash import sha256_crypt
from flask_bootstrap import Bootstrap
import csv  
import json
import sys
import datetime
import time
import os
from datetime import timedelta
#from signal import signal, SIGPIPE, SIG_DFL


#signal(SIGPIPE, SIG_DFL)
app = Flask(__name__)
Bootstrap(app)
app.secret_key = "super secret key"

@app.route('/section_data')
def section_data():
   conn, cur = connection()
   cur.execute('SELECT section FROM section')

   row_headers=[x[0] for x in cur.description] #this will extract row headers
   rv = cur.fetchall()
   json_data=[]
   for result in rv:
        json_data.append(dict(zip(row_headers,result)))
   return (json.dumps(json_data))

@app.route('/main/')
def main():
    return render_template("main.html")

@app.route('/add_money_in/')
def add_money_in():
    return render_template("add_money_in.html")

@app.route('/add_money_out/')
def add_money_out():
    return render_template("add_money_out.html")

@app.route('/login/', methods=["GET","POST"])
@app.route('/', methods=["GET","POST"])
def login():
    error=''
    error1=''
    try:
        if request.method == "POST":
            username = request.form['username']
            password = request.form['password']
            conn, cur = connection()
            x=cur.execute("SELECT * FROM user WHERE username=(%s)",(username,))
            if int(x) == 0 :
                error = 'User Not found'
            elif int(x) > 0 :
                conn, cur = connection()
                cur.execute("SELECT password FROM user WHERE username=(%s)",(username,))
                record=cur.fetchone()
                for row in record : 
                    if (password) == (row) :
                        session['name'] = username
                        return redirect(url_for('main'))
                    else :
                        error1 = 'Wrong password'
        return render_template("login.html", error = error,error1=error1)
    
    except Exception as e:
        
        return render_template("login.html", error = error,error1=error1)

@app.route('/register/', methods=["GET","POST"])
def register():
    error1=''
    error2=''
    error3=''
    error5=''
    error6=''
    if request.method == "POST":
        role=str(request.form["role"])
        name=request.form["name"]
        username=request.form["username"]
        password=request.form["password"]
        confirm=request.form["confirm"]
        domain=request.form["domain"]
        age=request.form["age"]
        gender=str(request.form["gender"])
        if domain == "1qazXSW@":

            if password == confirm :
                if name== "":
                    error1='Name is missing'
                if username == "":
                    error2='Username is missing'
                if age == "":
                    error3='age is missing'
                else:
                    conn, cur=connection()
                    cur.execute("INSERT INTO user (name,username,password,age,gender,role) VALUE(%s,%s,%s,%s,%s,%s)",(name,username,password,age,gender,role,))
                    conn.commit()
                    return redirect(url_for('login'))
            else:
                error5="Password not matched"
        else:
            error6="Wrong Domain Passowrd"
    return render_template("register.html",error5=error5,error6=error6,error1=error1,error2=error2,error3=error3)





if __name__== '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
