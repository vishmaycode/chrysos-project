from flask import Flask,render_template,redirect,url_for,request,session
import sqlite3
import random
from flask_sqlalchemy import SQLAlchemy
import random
from datetime import date

app=Flask(__name__)

app.config['SECRET_KEY']="HARD TO GUESS"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////home/master/Downloads/git-repos/my/chrysos/db/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db=SQLAlchemy(app)

class User(db.Model):
    __tablename__='user'
    U_ID=db.Column(db.Integer,primary_key=True)
    FU_NAME=db.Column(db.String)
    EMAIL=db.Column(db.String)
    P_NO=db.Column(db.Integer)
    GENDER=db.Column(db.String)
    U_NAME=db.Column(db.String)
    U_PASSWORD=db.Column(db.String)

class Investemnt(db.Model):
    __tablename__='investment'
    I_ID=db.Column(db.Integer,primary_key=True)
    GTYPE=db.Column(db.String)
    QUANTITY=db.Column(db.String)
    CASH=db.Column(db.Integer)
    DATE=db.Column(db.Date)
    U_ID=db.Column(db.Integer,db.ForeignKey('user.id'))

class Sent_Mail(db.Model):
    __tablename__='sent_mail'
    E_ID=db.Column(db.Integer,primary_key=True)
    EMAIL=db.Column(db.String)
    U_ID=db.Column(db.Integer,db.ForeignKey('user.id'))

class User_Add(db.Model):
    __tablename__='user_add'
    A_ID=db.Column(db.Integer,primary_key=True)
    U_ADD=db.Column(db.String)
    U_ID=db.Column(db.Integer,db.ForeignKey('user.id'))

@app.route("/")
@app.route("/main")
def main():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if(request.method=='POST'):
        r=""
        username=request.form['username']
        password=request.form['password']
        con=sqlite3.connect("/home/master/Downloads/git-repos/my/chrysos/db/database.db")
        c=con.cursor()
        c.execute("SELECT * FROM user WHERE U_NAME='"+username+"' and U_PASSWORD='"+password+"'")
        r=c.fetchall()
        for i in r:
            if(username==i[5] and password==i[6]):
                session['id']=i[0]
                session['loggedin']=True
                session['username']=i[5]
                return redirect(url_for("UP"))
    return render_template("login.html")

@app.route("/signup",methods=["GET","POST"])
def signup():
    if(request.method=='POST'):
        r=str(random.randint(100, 1000))
        if(request.form['username']!="" and request.form['fullname']!="" and request.form['email']!="" and request.form['phonenumber']!="" and request.form['gender']!="" and request.form['password']!="" and request.form['confirmpassword']!="" and request.form['password']==request.form['confirmpassword']):
            fname=request.form['fullname']
            email=request.form['email']
            pno=request.form['phonenumber']
            gender=request.form['gender']
            username=request.form['username']
            password=request.form['password']
            con=sqlite3.connect("/home/master/Downloads/git-repos/my/chrysos/db/database.db")
            c=con.cursor()
            c.execute("INSERT INTO user VALUES('"+r+"','"+fname+"','"+pno+"','"+email+"','"+gender+"','"+username+"','"+password+"')")
            con.commit()
            con.close()
            return redirect(url_for("login"))
    return render_template("signup.html")


@app.route("/more")
def more():
    return render_template("more.html")

# @app.route("/home")
# def home():
#     return render_template("OGI_home.html")
    

@app.route("/sell",methods=["GET","POST"])
def sell():
    s=session['id']
    shares=Investemnt.query.filter_by(U_ID=s)
    if(request.method=='POST'):
        if(request.form['id']!=""):
            id=str(request.form['id'])
            con=sqlite3.connect("/home/master/Downloads/git-repos/my/chrysos/db/database.db")
            c=con.cursor()
            c.execute("DELETE FROM investment WHERE I_ID='"+id+"'")
            con.commit()
            con.close()
    return render_template("OGI_SELL.html",shares=shares)
    

@app.route("/buy")
def buy():
    return render_template("OGI_BUY.html")
    

@app.route("/certificate",methods=["GET","POST"])
def certificate():
    r=str(random.randint(1,100))
    s=str(session['id'])
    if(request.method=='POST'):
        if(request.form['usermail']!=""):
            mail=request.form['usermail']
            con=sqlite3.connect("/home/master/Downloads/git-repos/my/chrysos/db/database.db")
            c=con.cursor()
            c.execute("INSERT INTO sent_mail VALUES('"+r+"','"+s+"','"+mail+"')")
            con.commit()
            con.close()
            return redirect(url_for('econfirmation'))
    return render_template("OGI_CERTIFY.html",)
    
    
@app.route("/HD",methods=["GET","POST"])
def HD():
    s=str(session['id'])
    r=str(random.randint(10000,10100))
    if(request.method=='POST'):
        if(request.form['address']!=""):
            addr=request.form['address']
            con=sqlite3.connect("/home/master/Downloads/git-repos/my/chrysos/db/database.db")
            c=con.cursor()
            c.execute("INSERT INTO user_add VALUES('"+r+"','"+s+"','"+addr+"')")
            con.commit()
            con.close()
    return render_template("OGI_HD.html")

@app.route("/UP")
def UP():
    s=session['id']
    d=User.query.filter_by(U_ID=s)
    a=User_Add.query.filter_by(U_ID=s)
    return render_template("OGI_UP.html",details=d,addr=a)


@app.route("/24k",methods=["GET","POST"])
def k24():
    if(request.method=='POST'):
        if(request.form['24kcash']!="" and request.form['24kweight']!=""):
            I_ID=str(random.randint(1000, 10000))
            U_UID=str(session['id'])
            GTYPE="24k"
            cash=request.form['24kcash']
            QUANTITY=request.form['24kweight']
            today=str(date.today())
            con=sqlite3.connect("/home/master/Downloads/git-repos/my/chrysos/db/database.db")
            c=con.cursor()
            c.execute("INSERT INTO investment VALUES('"+I_ID+"','"+U_UID+"','"+GTYPE+"','"+QUANTITY+"','"+cash+"','"+today+"')")
            con.commit()
            con.close()
            return redirect(url_for("debit"))
    return render_template("BUY_24k.html")

@app.route("/22k",methods=["GET","POST"])
def k22():
    if(request.method=='POST'):
        if(request.form['22kcash']!="" and request.form['22kweight']!=""):
            I_ID=str(random.randint(1000, 10000))
            U_UID=str(session['id'])
            GTYPE="22k"
            QUANTITY=request.form['22kweight']
            cash=request.form['22kcash']
            today=str(date.today())
            con=sqlite3.connect("/home/master/Downloads/git-repos/my/chrysos/db/database.db")
            c=con.cursor()
            c.execute("INSERT INTO investment VALUES('"+I_ID+"','"+U_UID+"','"+GTYPE+"','"+QUANTITY+"','"+cash+"','"+today+"')")
            con.commit()
            con.close()
            return redirect(url_for("debit"))
    return render_template("BUY_22k.html")


@app.route("/21k",methods=["GET","POST"])
def k21():
    if(request.method=='POST'):
        if(request.form['21kcash']!="" and request.form['21kweight']!=""):
            I_ID=str(random.randint(1000, 10000))
            U_UID=str(session['id'])
            GTYPE="21k"
            QUANTITY=request.form['21kweight']
            cash=request.form['21kcash']
            today=str(date.today())
            con=sqlite3.connect("/home/master/Downloads/git-repos/my/chrysos/db/database.db")
            c=con.cursor()
            c.execute("INSERT INTO investment VALUES('"+I_ID+"','"+U_UID+"','"+GTYPE+"','"+QUANTITY+"','"+cash+"','"+today+"')")
            con.commit()
            con.close()
            return redirect(url_for("debit"))
    return render_template("BUY_21k.html")


@app.route("/18k",methods=["GET","POST"])
def k18():
    print("18k debugging")
    if(request.method=='POST'):
        if(request.form['18kcash']!="" and request.form['18kweight']!=""):
            print("18k debugging 2")
            I_ID=str(random.randint(1000, 10000))
            U_UID=str(session['id'])
            GTYPE="18k"
            cash=request.form['18kcash']
            QUANTITY=request.form['18kweight']
            today=str(date.today())
            con=sqlite3.connect("/home/master/Downloads/git-repos/my/chrysos/db/database.db")
            c=con.cursor()
            c.execute("INSERT INTO investment VALUES('"+I_ID+"','"+U_UID+"','"+GTYPE+"','"+QUANTITY+"','"+cash+"','"+today+"')")
            con.commit()
            con.close()
            return redirect(url_for("debit"))
    return render_template("BUY_18k.html")


@app.route("/debit",methods=["GET","POST"])
def debit():
    if(request.method=="POST"):
        if(request.form["cardno"]!="" and request.form["month"]!="" and request.form["year"]!=""):
            return redirect(url_for("otp"))
    return render_template("debit.html")


@app.route("/otp",methods=["GET","POST"])
def otp():
    if(request.method=="POST"):
        if(request.form["otp"]!=""):
            return redirect(url_for("pconfirmation"))
    return render_template("otp.html")

@app.route("/pconfirm")
def pconfirmation():
    return render_template("pconfirmation.html")

@app.route("/econfirm")
def econfirmation():
    return render_template("econfirmation.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("main"))


@app.route("/admin",methods=["GET","POST"])
def admin():
    if(request.method=="POST"):
        if(request.form['adminid']=="ADMIN" and request.form['adminpassword']=="ADMIN"):
            user=User.query.all()
            mail=Sent_Mail.query.all()
            user_add=User_Add.query.all()
            return render_template("admin_data.html",user=user,mail=mail,user_add=user_add)
    return render_template("admin.html")


app.run(debug=True)