
from enum import IntEnum
from main.utils import round6, print_colored, print_solution
from main.operations import is_int
from .fractions import get_fraction_string, reduce_fraction, print_fraction

class Solutions(IntEnum):
	ZERO = 0
	POSITIVE1 = 1
	POSITIVE2 = 2
	NEGATIVE = -1
	DEGREE1 = 3

def steps_positive(list, D_root, numerator, sign):
	step1 = f"({round6(-list[1])} {sign} {(round6(D_root))})/(2 * {round6(list[2])})"
	step2 = f"{numerator}/{round6(2*list[2])}"
	result = f"{round6(numerator/round6(2*list[2]))}"
	if is_int(D_root) or is_int(numerator):
		fraction_str = get_fraction_string(numerator, (2*list[2]))[0]
		if result == fraction_str or step2 == fraction_str:#result is integer or the fraction is irreducible
			print_colored(f'(-b {sign} \u221AD)/2a = {step1} = {step2} = {result}', "purple")
		else:
			print_colored(f'(-b {sign} \u221AD)/2a = {step1} = {step2} = {fraction_str} = {result}', "purple")
	else:
		print_colored(f'(-b {sign} \u221AD)/2a = {step1} = {step2} = {result}', "purple")

def steps_zero(list, D_root):
	(numerator, denominator) = reduce_fraction(-list[1], 2*list[2])
	s = round6(numerator/denominator)
	if s < 0:
		sign = "-"
	else:
		sign = ""
	step1 = f"{sign}{abs(round6(list[1]))}/(2 * {abs(round6(list[2]))})"
	step2 = f"{sign}{abs(round6(list[1]))}/{abs(2*list[2])}"
	step3 = f"{sign}{abs(round6(numerator))}/{abs(round6(denominator))}"
	if step2 == step3:
		print_colored(f'-b/2a = {step1} = {step2} = {s}', "purple")
	else:
		print_colored(f'-b/2a = {step1} = {step2} = {step3} = {s}', "purple")

def steps_degree1(list):
	(numerator, denominator) = reduce_fraction(-list[0],list[1])
	print_fraction(numerator, denominator)
	s = round6(numerator/denominator)
	if s < 0:
		sign = "-"
	else:
		sign = ""
	step1 = f"{sign}{abs(round6(list[0]))}/{abs(round6(list[1]))}"
	step2 = f"{sign}{abs(round6(numerator))}/{abs(round6(denominator))}"
	if step1 == step2:
		print_colored(f"-b/a = {step1} = {s}", "purple")
	else:
		print_colored(f"-b/a = {step1} = {step2} = {s}", "purple")

def print_solution_steps(type, list, D_root):
	text=""
	match type:
		case Solutions.POSITIVE1:
			text = "Discriminant is strictly positive, the two solutions are:"
			sign = "+"
			numerator = round6(-list[1] + D_root)
		case Solutions.POSITIVE2:
			sign = "-"
			numerator = round6(-list[1] - D_root)
		case Solutions.ZERO:
			text = "Discriminant equals zero, the solution is:"
		case Solutions.DEGREE1:
			text = "Notation: ax + b = 0\nThe solution is:"
	if text:
		print_colored(text, "blue")
	if type == Solutions.POSITIVE1 or type == Solutions.POSITIVE2:
		steps_positive(list, D_root, numerator, sign)
	elif type == Solutions.ZERO:
		steps_zero(list, D_root)
	elif type == Solutions.DEGREE1:
		steps_degree1(list)