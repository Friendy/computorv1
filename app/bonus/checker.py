import re, sys
from .error import Types, ErrorTypes, InputError, print_error, raise_input_error, raise_sign_error

#  a * x^p
# term pattern
# returns next pos after the term
def sign_check(input, type):
	end = 3
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
	i += term_check(input[i:], Types.RIGHT)
	while i <= end:
		i += term_check(input[i:], Types.ALL)