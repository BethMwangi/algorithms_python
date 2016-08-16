# You are presented with two arrays, all containing positive integers. 
# One of the arrays will have one extra number, see below:

# [1,2,3] and [1,2,3,4] should return 4

# [4,66,7] and [66,77,7,4] should return 77




#define a function find_missing that takes two lists as paramaters
def find_missing(alist1, alist2):
	if len(alist1) == 0 and len(alist2) == 0: #checks if the lists are empty
		return 'the list is empty'
	elif len(alist1) == len(alist2): #checks if lists have same number of items
		for num in alist1:
			if num in alist2:
				return 'the lists are similar'
	else:
		if len(alist1) < len(alist2): #if the second list has more numbers it loops through the numbers first 
			for num in alist2:
				if num not in alist1:
					return num
		elif len(alist2) < len(alist1):
			for num in alist1:
				if num not in alist2:
					return num

print (find_missing([], [])) #test cases
print (find_missing([4], [4]))
print (find_missing([1,2,3], [1,2,3,4])) 
print (find_missing([4,66,7], [66,77,7,4])) #call the function

