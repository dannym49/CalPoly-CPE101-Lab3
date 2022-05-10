def max_101(x, y):
	if x > y:
		return x 
	else:
		return y

def max_of_three(x,y,z):
	if x >= y and x >= z:
		answer = x 
	elif y >= x and y >= z:
		answer = y
	else:
		answer = z
	return answer

def rental_late_fee(x):
	fee = 0
	if x <= 0:
		fee = 0
	elif 0< x <= 9:
		fee = 5
	elif 9< x <= 15:
		fee = 7
	elif 15 < x <= 24:
		fee = 19
	else:
		fee = 100
	return fee


