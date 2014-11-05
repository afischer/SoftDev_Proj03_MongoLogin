from flask import Flask, render_template, request
from utils import loginChecker
#from pymongo import Connection

app = Flask(__name__)

#conn = Connection()
#db = conn.userDatabase

def verify(uName, pword):
    if(db.userData.find({userName: uName}) == None):
        return True;
    else:
        return False;


def addUser(uName, pword, fName, lName, em):
    if (verify(uName, pword)):
        db.userData.insert({userName: uName, password: pword, firstName: fName, lastName: lName, email: em})
        print "Added User " + fName + " " + lName
        return True
    else:
        print "This username is already taken."
        return False


#addUser("Jane", "Doe", "Jane", "Doe", "jdoe@schools.nyc.gov")

@app.route("/login", methods=['POST', 'GET'])
@app.route("/", methods=['POST', 'GET'])
def login():
    if request.method=='GET':
        return render_template("login.html", nextPage="/")
    else:
        uName = request.form["uName"]
        pword = request.form["pword"]
        if (checkLogin(uName, pword)):
            print uName
            print pword
            return "hi"
        else:
            return "boo"

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method=="GET":
        return render_template("signup.html", nextPage="/")
    else:
        em = request.form["email"]
        fName = request.form["fName"]
        lName = request.form["lName"]
        uName = request.form["uName"]
        pword = request.form["pword"]
        confPword = request.form["confPword"]
        if (addUser(uName, pword, fName, lName, em)):
            return render_template("login.html")
        else:
            return render_template("signup.html")



@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

if __name__=="__main__":
    app.debug=True
    app.run()
