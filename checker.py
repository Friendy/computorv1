import re, sys, textwrap
from enum import IntEnum
from utils_bonus import print_select
from utils import print_colored
class InputError(Exception):
	pass

class Types(IntEnum):
	FIRST = 1
	MULT = 0
	EQUAL = -1
	ALL = 3
	RIGHT = 4

class ErrorTypes(IntEnum):
	COEF_MISSING = 100
	COEFF_SPACE_MISSING = 101
	COEF_FORMAT = 102
	INDETERMINATE = 103
	FORBIDDEN = 104
	EQUAL_SIGN_COUNT = 105

def raise_sign_error(type):
	match type:
		case Types.FIRST | Types.RIGHT:
			text = "The first term on the left side or the right side (after the equal sign) of the polinomial should start either with a minus, followed by a space: \"- \" or with a number"
		case Types.MULT:
			text = "A coefficient should be followed by the multiplication operator surrounded with spaces:\' * \'"
		case Types.EQUAL:
			text = "An equal sign should be surrounded with spaces \' = \'"
		case _:
			text = "Any term of the polinomial, except for the first term on the left/right side should be preceeded by a plus or a minus surrounded with spaces \" - \", \" + \"."
	wrapped_text = textwrap.fill(text, 70)
	raise InputError(wrapped_text)

def raise_input_error(type):
	match type:
		case ErrorTypes.COEF_MISSING:
			text = "A coefficient might be missing"
		case ErrorTypes.COEFF_SPACE_MISSING:
			text = "A space after the coefficient might be missing"
		case ErrorTypes.COEF_FORMAT:
			text = "A coefficient has a wrong format or a space after it is missing."
		case ErrorTypes.INDETERMINATE:
			text = "The indeterminant part has the \"X^p\" format, where X is imdeterminant"
		case ErrorTypes.FORBIDDEN:
			text = "The input contains a forbidden character. Allowed characters: all digits, space, *, -, +, =, ^, ."
		case ErrorTypes.EQUAL_SIGN_COUNT:
			text = "The polinomial has no or more than one eqal signs"
	wrapped_text = textwrap.fill(text, 70)
	raise InputError(wrapped_text)

def print_error(error, input, start):
	print_colored("Error: ", "red", endline="")
	print_colored(error, "blue")
	if input:
		if start == Types.FIRST:
			print_select("", input[0], input[1:])
		else:
			print_select("...", input[0], input[1:])

def print_tip(type):
	match type:
		case ErrorTypes.COEF_MISSING:
			text = "A coefficient might be missing"
		case ErrorTypes.COEFF_SPACE_MISSING:
			text = "A space after the coefficient might be missing"
		case ErrorTypes.COEF_FORMAT :
			text = "A coefficient is an integer or a float number. It should have no leading zeros, that is: 00.056 should be replaced with 0.056"
		# case ErrorTypes.:
		# 	text = "Any term of the polinomial except for the first term should be preceeded by one of the following operators. An operator should be preceeded and followed by space"
	wrapped_text = textwrap.fill(text, 70)
	print_colored("Tip: ", "purple", endline="")
	print_colored(wrapped_text, "purple")
#  a * x^p
# term pattern
# returns next pos after the term
def sign_check(input, type):
	end = 3
	# print(input)
	match type:
		case Types.FIRST | Types.RIGHT:
			sign_pattern = r'^(\-\s)$'
			end = 2
		case Types.MULT:
			sign_pattern = r'^\s\*\s$'
		case Types.EQUAL:
			sign_pattern = r'^\s\=\s$'
		case _:
			sign_pattern = r'^\s[\+,\-]\s$'
	try:
		x = re.search(sign_pattern, input[:end])
		if x:
			return x.span()[1]
		else:
			if type == Types.FIRST or Types.RIGHT:
				if input and input[0].isnumeric():
					return 0
				else:
					raise_sign_error(type)
			else:
				raise_sign_error(type)
	except InputError as e:
			print_error(e, input , type)
			exit(-1)

def check_coeff(input, type):
	try:
		if len(input) == 0:
			raise_input_error(ErrorTypes.COEF_MISSING)
		end = input.find(r' ')
		if end == -1:
			raise_input_error(ErrorTypes.COEFF_SPACE_MISSING)
		else:
			pattern = r'^(0|[1-9]\d*)(\.\d+)?$'
			x = re.search(pattern, input[:end])
		if x:
			return x.span()[1]
		else:
			raise_input_error(ErrorTypes.COEF_FORMAT)
	except InputError as e:
			print_tip(ErrorTypes.COEF_FORMAT)
			print_error(e, input, type)
			exit(-1)


def check_xpower(input):
	pattern = r'^X\^(0|[1-9]\d*)'
	x = re.search(pattern, input)
	if x:
		return x.span()[1]
	else:
		try:
			raise_input_error(ErrorTypes.INDETERMINATE)
		except InputError as e:
			print_error(e, input, Types.ALL)
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
	pos = 0
	try:
		if input.count("=") != 1:
			raise_input_error(ErrorTypes.EQUAL_SIGN_COUNT)
		x = re.search(r'[^X\*\-\=\+\^\s\.\d]', input)
		if x:
			pos = x.span()[0]
			raise_input_error(ErrorTypes.FORBIDDEN)
	except InputError as e:
			if pos == 0:
				print_error(e, input[pos:], Types.FIRST)
			else:
				print_error(e, input[pos:], Types.ALL)
			sys.exit(-1)
	i = 0
	eq_ind = input.find('=')
	end = len(input) - 1
	while i < eq_ind - 1:
		i += term_check(input[i:], i + 1)
	i += sign_check(input[i:], Types.EQUAL)
	# print("i", i)
	i += term_check(input[i:], Types.RIGHT)
	# print("i after chck", i)
	while i <= end:
		i += term_check(input[i:], Types.ALL)