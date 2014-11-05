import pymongo


conn = pymongo.MongoClient()
db = conn.userDatabase


def addUser(uName, pword, fName, lName, em):
    if (verify(uName, pword)):
        db.userData.insert({'userName': uName, 'password': pword, 'firstName': fName, 'lastName': lName, 'email': em})
        print "Added User " + fName + " " + lName
        return True
    else:
        print "This username is already taken."
        return False

def verify(uName, pword):
    if(db.userData.find({'userName': uName}) == None):
        return True;
    else:
        return False;
