import re, sys
from enum import IntEnum
from utils_bonus import print_select
class InputError(Exception):
	pass

class Types(IntEnum):
	FIRST = 1
	MULT = 0
	EQUAL = -1
	ALL = 3

def raise_input_error(type):
	match type:
		case Types.FIRST:
			raise InputError("The polinomial should start either with the minus operator \"-\" or with a number")
		case Types.MULT:
			raise InputError("A coefficient should be followed by the multiplication operator surrounded with spaces\' * \'")
		case Types.EQUAL:
			raise InputError("spaces\' = \'")
		case _:
			raise InputError("Any term of the polinomial except for the first term should be preceeded by one of the following operators. An operator should be preceeded and followed by space")
#  a * x^p
# term pattern
# returns next pos after the term
def sign_check(input, type):
	end = 3
	match type:
		case Types.FIRST:
			sign_pattern = r'^(\-\s)$'
			end = 2
		case Types.MULT:
			sign_pattern = r'^\s\*\s$'
		case Types.EQUAL:
			sign_pattern = r'^\s\=\s$'
		case _:
			sign_pattern = r'^\s[\+,\-]\s$'
	# if type == Types.FIRST:

	# elif type == Types.MULT:
	# 	sign_pattern = r'^\s\*\s$'
	# elif type == Types.EQUAL:
	# 	sign_pattern = r'^\s\=\s$'
	# else:
	# 	sign_pattern = r'^\s[\+,\-]\s$'
	try:
		x = re.search(sign_pattern, input[:end])
		if x:
			return x.span()[1]
		else:
			if type == Types.FIRST:
				if input[0].isnumeric():
					return 0
				else:
					raise_input_error(type)
			else:
				raise_input_error(type)
	except InputError as e:
			print(f"Error: {e}")
			if type == Types.FIRST:
				print_select("", input[0], input[1:])
			else:
				print_select("...", input[0], input[1:])
			exit(-1)

def check_coeff(input, type):
	try:
		if len(input) == 0:
			raise InputError("A coefficient is missing")
		# print("len", len(input))
		end = input.find(r' ')
		if end == -1:
			raise InputError("A space after the coefficient is missing")
		else:
			pattern = r'^(0|[1-9]\d*)(\.\d+)?$'
			x = re.search(pattern, input[:end])
		if x:    
			return x.span()[1]
		else:
			raise InputError("a coefficient is an integer or a float number. \n It should have no leading or trailing meaningless zeros , that is: 00.05600 should be replaced with 0.056")
	except InputError as e:      
			start = "..."
			if type == Types.FIRST:
				start = ""
			if len(input) != 0:
				print_select(start, input[0], input[1:])
			print(f"Error: {e}")
			exit(-1)


def check_xpower(input):
	pattern = r'^X\^(0|[1-9]\d*)'
	x = re.search(pattern, input)
	if x:
		return x.span()[1]
	else:
		try:
			raise InputError("the indeterminant is X \"X^p\"")
		except InputError as e:
			print(f"Error: {e}")
			exit(-1)

	# the indeterminant is X "X^p"
def term_check(term, type):
	i = sign_check(term, type)
	i += check_coeff(term[i:], type)
	i += sign_check(term[i:], Types.MULT)
	i += check_xpower(term[i:])
	return i

# def print_select(start, colored, end):
#     print(f"{start}{'\033[91m\033[4m\033[1m'}{colored}{'\033[0m'}{end}")

# 2 parts seperated by eq, 
# each part consists of terms 
# each term starts with number, then multiplication sign then x hat pow
# input starts whith a term or a minus
# only one eq sign and at least one term after it

def input_check(input):
	try:
		if input.count("=") != 1:
			raise InputError("no or more than one eqal signs")
		x = re.search(r'[^X\*\-\=\+\^\s\.\d]', input)
		if x:
			pos = x.span()[0]
			raise InputError("the input contains forbidden character, allowed characters: all digits, space, *, -, +, =, ^, .")
	except InputError as e:
			print(f"Error: {e}")
			sys.exit(-1)
	i = 0
	eq_ind = input.find('=')
	end = len(input) - 1
	while i < eq_ind - 1:
		i += term_check(input[i:], i + 1)
	i += sign_check(input[i:], Types.EQUAL)
	print("i", i)
	i += term_check(input[i:], Types.FIRST)
	while i <= end:
		i += term_check(input[i:], Types.ALL)