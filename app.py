from flask import Flask, render_template, request
from utils import loginChecker, dbManager
import pymongo

app = Flask(__name__)


conn = pymongo.MongoClient()
db = conn.userDatabase


dbManager.addUser("Jane", "Doe", "Jane", "Doe", "jdoe@schools.nyc.gov")

@app.route("/login", methods=['POST', 'GET'])
@app.route("/", methods=['POST', 'GET'])
def login():
    if request.method=='GET':
        return render_template("login.html", nextPage="/")
    else:
        uName = request.form["uName"]
        pword = request.form["pword"]
        if (loginChecker.checkLogin(uName, pword)):
            print uName
            print pword
            return "yay"
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
        if (dbManager.addUser(uName, pword, fName, lName, em)):
            print "ADDED" + fName + " " + lName
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
