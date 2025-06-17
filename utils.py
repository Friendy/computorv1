from operations import pow2, square_root, round6
import time

# adding coefficient to the array
# appending nulls and the value to the array so that
def  add_coef(arr, power, val):
	last_ind = len(arr) - 1
	while power > last_ind + 1:
		arr.append(0)
		last_ind += 1
	if power <= last_ind:
		arr[power] += val
	else:
		arr.append(val)

# getting the coefficient of the power given the power index
def get_coef(input_data, pow_ind):
	end = input_data.rfind(" * ", 0, pow_ind) - 1;
	start = input_data.rfind(" ", 0, end) + 1
	coefString = input_data[start: end + 1]
	if (coefString.rfind(".") >= 0):
		coef  = float(coefString)
	else:
		coef = int(coefString)
	if input_data[start - 2] == '-':
		coef = -coef
	return coef

# because in the reduced array all coefficients are on the left side
# when we process the right side we multiply it by -1 
def reduction(input_data):
	# initializing an array where the reduced data will be stored  
	# the form: coefficient[power]	
	reduced_arr = []
	# finding positions of the equal sign and the end
	last_ind = len(input_data) - 1
	eq_ind = input_data.find('=')
	i = 0
	while i <= last_ind:
		if input_data[i] == '^':
			pow = int(input_data[i + 1])
			val = get_coef(input_data, i)
			if i > eq_ind:
				val = - 1 * val
			add_coef(reduced_arr, pow, val)
		i += 1
	return reduced_arr

# printing the reduced equation to the screen based on reduced array
def print_reduced(arr, max_pow):
	i = 0
	text = ""
	while  i <= max_pow:
		cur_coef = arr[i]
		if arr[i] < 0:
			text += ' - '
			cur_coef = - cur_coef
		elif i > 0:
			text += ' + '
		text += str(cur_coef) + " * X^" + str(i)
		i += 1
	text += " = 0"
	print("Reduced form:", text.strip())

def getDegree(arr):
	length = len(arr)
	last_ind = length - 1
	while last_ind > 0 and arr[last_ind] == 0: 
		last_ind -= 1
	return last_ind
  
def solution(arr, degree):
	if degree == 2:
		D = pow2(arr[1]) - 4*arr[2]*arr[0]
		if D > 0:
			D_root = square_root(D)
			s1 = (-arr[1] + D_root)/(2*arr[2])
			s2 = (-arr[1] - D_root)/(2*arr[2])
			print("Discriminant is strictly positive, the two solutions are:", round6(s1), round6(s2), sep="\n")			
		elif D == 0:
			print("Discriminant equals zero, the solution is:", round6(-arr[1]/2*arr[2]))
		else:
			print("Discriminant is strictly negative, there is no real solution:")
	elif degree == 1:
		print("The solution is:", -arr[0]/arr[1], sep="\n")
	elif degree == 0:
		if (arr[0] == 0):
			print("Any real number is a solution")
		else:
			print("This equation has no solutions")
	else:
		print("The polynomial degree is strictly greater than 2, I can't solve.")
		
			


	




