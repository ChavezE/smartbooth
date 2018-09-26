import pyrebase

def getDB():
	config = {
    "apiKey": "AIzaSyAq9xA-sjwtOmye3j_xzURxacHP6qknLOg",
    "authDomain": "photoboot-e2b33.firebaseapp.com",
    "databaseURL": "https://photoboot-e2b33.firebaseio.com",
    "storageBucket": "photoboot-e2b33.appspot.com",
	}

	firebase = pyrebase.initialize_app(config)
	db = firebase.database()

	return db