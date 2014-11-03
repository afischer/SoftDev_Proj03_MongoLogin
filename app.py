from flask import Flask, render_template, request
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
    else:
        print "This username is already taken."


#addUser("Jane", "Doe", "Jane", "Doe", "jdoe@schools.nyc.gov")

@app.route("/", methods=['POST', 'GET'])
def login():
    return render_template("login.html", nextPage="/")

@app.route("/login", methods=['POST', 'GET'])
def login2():
    return render_template("login.html", nextPage="/")

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    return render_template("signup.html", nextPage="/")


@app.route("/about")
def about():
    return render_template("about.html")



if __name__=="__main__":
    app.debug=True
    app.run()
