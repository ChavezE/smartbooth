import re
import pyrebase

config = {
  "apiKey": "AIzaSyAq9xA-sjwtOmye3j_xzURxacHP6qknLOg",
  "authDomain": "photoboot-e2b33.firebaseapp.com",
  "databaseURL": "https://photoboot-e2b33.firebaseio.com",
  "storageBucket": "photoboot-e2b33.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

correctMat = '\A(A|a)\d{8}$'

def validateMatricule(mat):

	# size of mat should be fixed to 9 chars
	if len(mat) != 9:
		return False

	# returns None if no match
	result = re.search(correctMat, mat)
	if result:
		return True
	else:
		return False

# isValid = validateMatricule('A00816752')

def validateCareer(career):
	receivedCareerUpperCase = str(career).upper().strip()

	if not receivedCareerUpperCase:
		return False;

	all_careers = db.child("careers").get()

	careerNameList = []

	for user in all_careers.each():
		careerNameList = user.val()

	for careerName in careerNameList:
		careerNameUpperCase = str(careerName).upper()
		if careerNameUpperCase == receivedCareerUpperCase:
			return True

	return False
