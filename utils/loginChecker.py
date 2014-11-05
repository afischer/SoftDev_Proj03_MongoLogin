import pymongo


conn = pymongo.MongoClient()
db = conn.userDatabase


def checkLogin(uName, pword):
    if(db.userData.count({'userName': uName, 'password': pword}) > 0):
         return True;
    else:
         return False;
