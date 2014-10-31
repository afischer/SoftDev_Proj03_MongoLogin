from flask import Flask, render_template, request
from pymongo import Connection

app = Flask(__name__)

conn = Connection()
db = conn.userDatabase

def addUser(uName, pword, fName, lName, em):
    db.userData.insert({userName: uName, password: pword, firstName: fName, lastName: lName, email: em})
    print "Added User " + fName + " " + lName

addUser("Jane", "Doe", "Jane", "Doe", "jdoe@schools.nyc.gov")

#@app.route("/", methods=['POST', 'GET'])
#def login():
#    render_template("login.html")


if __name__=="__main__":
    app.debug=True
    app.run()
