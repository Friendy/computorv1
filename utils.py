from operations import pow2, square_root, round6
import time
from enum import IntEnum

class Solutions(IntEnum):
	ZERO = 0
	POSITIVE = 1
	NEGATIVE = -1
	POWER1 = 2

# 94 blue 95 purple 96 bright blue 91 red

def print_colored(text, color, endline = "\n"):
	match color:
		case "green":
			tag = '\033[92m'
		case "red":
			tag = '\x1b[6;37;47m'
		case "blue":
			tag = '\033[96m'
		case "brown":
			tag = '\033[97m'
	print(f"{tag}{text}{'\033[0m'}", end = endline)

# adding coefficient to the list
# appending nulls if necessary
def  add_coef(list, power, val):
	last_ind = len(list) - 1
	while power > last_ind + 1:
		list.append(0)
		last_ind += 1
	if power <= last_ind:
		list[power] += val
	else:
		list.append(val)

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
	reduced_list = []
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
			add_coef(reduced_list, pow, val)
		i += 1
	return reduced_list

# printing the reduced equation to the screen based on reduced array
def print_reduced(list, max_pow):
	i = 0
	text = ""
	while  i <= max_pow:
		cur_coef = list[i]
		if list[i] < 0:
			text += ' - '
			cur_coef = - cur_coef
		elif i > 0:
			text += ' + '
		text += str(cur_coef) + " * X^" + str(i)
		i += 1
	text += " = 0"
	print_colored("Reduced form: ", "blue", endline="")
	print_colored(text.strip(), "green")

def getDegree(list):
	length = len(list)
	last_ind = length - 1
	while last_ind > 0 and list[last_ind] == 0:
		last_ind -= 1
	return last_ind

def print_solution(type, sol_tuple):
	match type:
		case Solutions.POSITIVE:
			text = "Discriminant is strictly positive, the two solutions are:"
		case Solutions.ZERO:
			text = "Discriminant equals zero, the solution is:"
		case Solutions.POWER1:
			text = "The solution is:"
	print_colored(text, "blue")
	if type == Solutions.POSITIVE:
		print_colored(f"{round6(sol_tuple[0])}\n{round6(sol_tuple[1])}", "green")
	else:
		print_colored(f"{round6(sol_tuple)}", "green")

def solution(list, degree):
	if degree == 2:
		D = pow2(list[1]) - 4*list[2]*list[0]
		if D > 0:
			D_root = square_root(D)
			print_solution(Solutions.POSITIVE, ((-list[1] + D_root)/(2*list[2]), (-list[1] - D_root)/(2*list[2])))
		elif D == 0:
			print_solution(Solutions.ZERO, (-list[1]/2*list[2]))
		else:
			print_colored("Discriminant is strictly negative, there is no real solution:", "blue")
	elif degree == 1:
		print_solution(Solutions.POWER1, (-list[0]/list[1]))
	elif degree == 0:
		if (list[0] == 0):
			print_colored("Any real number is a solution", "blue")
		else:
			print_colored("This equation has no solutions", "blue")
	else:
		print_colored("The polynomial degree is strictly greater than 2, I can't solve.", "blue")



