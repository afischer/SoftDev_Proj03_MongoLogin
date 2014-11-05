import pymongo


conn = pymongo.MongoClient()
db = conn.userDatabase


def checkLogin(uName, pword):
    if(db.userData.find({'userName': uName, 'password': pword}).count() > 0):
         return True;
    else:
         return False;
