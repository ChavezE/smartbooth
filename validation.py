import re

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
	# To do:
	# Look for a JSON or similar file in Database and compare
	# for an existing instance
	
	if len(career) != 3 or len(career) != 4:
		return False
	return True

