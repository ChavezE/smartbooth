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
	
isValid = validateMatricule('00816752')
print(isValid)