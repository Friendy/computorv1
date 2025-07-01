from operations import pow2, square_root, round6
import time

# 94 blue 95 purple 96 bright blue 91 red

def print_colored(text, color, endline = "\n"):
	match color:
		case "green":
			tag = '\033[92m'
		case "red":
			tag = '\x1b[6;37;47m'
		case "blue":
			tag = '\033[96m'
	print(f"{tag}{text}{'\033[0m'}", end = endline)

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
	if (coefString.find(".") >= 0):
		coef  = float(coefString)
	else:
		coef = int(coefString)
	if start - 2 >= 0 and input_data[start - 2] == '-':
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
			end = input_data.find(" ", i)
			if end > 0:
				pow = int(input_data[i + 1 : end])
			else:
				pow = int(input_data[i + 1 :])
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
		if cur_coef != 0 or max_pow == 0:
			if arr[i] < 0:
				text += ' - '
				cur_coef = - cur_coef
			elif i > 0:
				text += ' + '
			text += str(cur_coef) + " * X^" + str(i)
		i += 1
	text += " = 0"
	print_colored("Reduced form: ", "blue", endline="")
	print_colored(text.strip(), "green")

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
			print_colored("Discriminant is strictly positive, the two solutions are:", "blue")
			print_colored(f"{round6(s1)}\n{round6(s2)}", "green")
		elif D == 0:
			print_colored("Discriminant equals zero, the solution is:", "blue")
			print_colored(f"{round6(-arr[1]/2*arr[2])}", "green")
		else:
			print_colored("Discriminant is strictly negative, there is no real solution:", "blue")
	elif degree == 1:
		print_colored("The solution is:", "blue")
		print_colored(f"{round6(-arr[0]/arr[1])}", "green")
	elif degree == 0:
		if (arr[0] == 0):
			print_colored("Any real number is a solution", "blue")
		else:
			print_colored("This equation has no solutions", "blue")
	else:
		print_colored("The polynomial degree is strictly greater than 2, I can't solve.", "blue")



