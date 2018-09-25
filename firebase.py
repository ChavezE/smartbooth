import pyrebase

config = {
    "apiKey": "AIzaSyAq9xA-sjwtOmye3j_xzURxacHP6qknLOg",
    "authDomain": "photoboot-e2b33.firebaseapp.com",
    "databaseURL": "https://photoboot-e2b33.firebaseio.com",
    "projectId": "photoboot-e2b33",
    "storageBucket": "photoboot-e2b33.appspot.com",
    "messagingSenderId": "193395117022"
}


firebase = pyrebase.initialize_app(config)
db = firebase.database()

users = db.child("Students").order_by_child("carrera").get()

print (users.val())
