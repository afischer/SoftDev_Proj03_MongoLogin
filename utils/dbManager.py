import pymongo


conn = pymongo.MongoClient()
db = conn.userDatabase


def addUser(uName, pword, confPword, fName, lName, em):
    if (verify(uName, pword) and compPword(pword, confPword)):
        db.userData.insert({'userName': uName, 'password': pword, 'firstName': fName, 'lastName': lName, 'email': em})
        print "Added User " + fName + " " + lName
        return True
    else if (compPword(pword, confPword)):
        print "This username is already taken."
        return False
    else if (verify(uName, pword)):
        print "The passwords do not match."
        return False
    else:
        print "The username is already taken and the paswords do not match."
        return False
        
def compPword(pword, confPword):
    if (pword == confPword):
        return True
    else:
        return False

def verify(uName, pword):
    if(db.userData.find({'userName': uName}) == None):
        return True;
    else:
        return False;
