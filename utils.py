import math, time

def printk():
	print('k')

# def round6(n):
# 	# s = 
# 	return int(n*1000000) / 1000000

def round6(n):
	if n < 0:
		s = str(-n)
	else:
		s = str(n)
	point = s.rfind(".")
	digit = int(s[point + 7])
	s = s[:point + 7]
	f = float(s)
	if digit >= 5:
		f = f + 0.000001
	if n < 0:
		f = -f
	print(f)
	return f

# appending nulls and the value to the array so that
def append_ind(arr, ind, last_ind, val):
	while ind > last_ind + 1:
		arr.append(0)
		last_ind += 1
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
def reduction(input_data, arr, start_ind, last_ind):
	i = start_ind
	side = -1
	if start_ind == 0:
		side = 1
	while i <= last_ind:
		if input_data[i] == '^':
			pow = int(input_data[i + 1])
			val = side * get_coef(input_data, i)

			# if the last power in the array is less than the current power 
			# we fill the empty positions with nulls
			if pow > len(arr) - 1:
				append_ind(arr, pow, len(arr) - 1, val)
			else:
				arr[pow] += val
		i += 1
	return arr

# printing the reduced equation to the screen
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

def pow2(n):
	return n*n


def square_root(n):
	if n == 1:
		return 1
	if n > 1:
		min = 0
		max = n
	else:
		min = n
		max = 1
	candidate = min + (max - min)/2
	temp_pow = pow2(candidate)
	while (temp_pow != n):
		if temp_pow > n:
			max = candidate;
		else:
			min = candidate;
		old_candidate = candidate
		candidate = min + (max - min)/2
		if candidate == old_candidate:
			return candidate
		temp_pow = pow2(candidate)
	return candidate


def solution(arr, degree):
	if degree == 2:
		D = pow(arr[1], 2) - 4*arr[2]*arr[0]
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
		
			


	




