import textwrap
from enum import IntEnum
from .utils import print_select
from main.utils import print_colored
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
			text = "The first term on the left side or the right side (after the equal sign) of the  polynomial should start either with a minus, followed by a space: \"- \" or with a number"
		case Types.MULT:
			text = "A coefficient should be followed by the multiplication operator surrounded with spaces:\' * \'"
		case Types.EQUAL:
			text = "An equal sign should be surrounded with spaces \' = \'"
		case _:
			text = "Any term of the  polynomial, except for the first term on the left/right side should be preceeded by a plus or a minus surrounded with spaces \" - \", \" + \"."
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
			text = "The  polynomial has no or more than one eqal signs"
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