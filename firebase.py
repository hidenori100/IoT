import pyrebase
from pillout import pillout




config = {
    "apiKey": "AIzaSyBm6XT-Di3g-Lupenz4xkDu9YtBXJTiUgM",
    "authDomain": "iotprog.firebaseapp.com",
    "databaseURL": "https://iotprog-default-rtdb.firebaseio.com/",
    "projectId": "iotprog",
    "storageBucket": "iotprog.appspot.com",
    "messagingSenderId": "391748413180",
    "appId":"1:391748413180:web:d2f937dea976143b0e9979",
    "measurementId": "G-K0VRJJQR48"

};


firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
database = firebase.database()
while(True) :
    a = pillout()
    print (a)
    database.child("DB object name")
    data = {"key1": a}
    database.set(data)
