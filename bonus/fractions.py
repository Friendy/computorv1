
from main.utils import round6, print_colored, print_solution
from main.operations import is_int

def isdenominator(candidate, n):
	r = n/candidate
	return is_int(r)

def reduce_fraction(numerator, denominator):
	if abs(numerator) > abs(denominator):
		max = int(denominator)
	else:
		max = int(numerator)
	d = 2
	while d <= abs(max):
		while isdenominator(d, numerator) and isdenominator(d, denominator):
			numerator = numerator/d
			denominator = denominator/d
		d += 1
	return (numerator, denominator)

# prints a fraction and its decimal version if it does not reduce to integer
def print_fraction(numerator, denominator):
	number = round6(numerator/denominator)
	sign = ""
	if number < 0:
		sign = "-"
	if numerator == 0:
		print_colored(f"0", "green")
	elif abs(denominator) == 1:
		print_colored(f"{sign}{int(abs(numerator))}", "green")
	else:
		print_colored(f"{sign}{int(abs(numerator))}/{int(abs(denominator))} ({number})", "green")

# get formatted string of a reduced fraction
def get_fraction_string(numerator, denominator):
	(numerator, denominator) = reduce_fraction(int(numerator), int(denominator))
	number = round6(numerator/denominator)
	sign = ""
	if number < 0:
		sign = "-"
	if numerator == 0:
		return ("0", "0")
	elif abs(denominator) == 1:
		return (f"{sign}{int(abs(numerator))}", f"{sign}{int(abs(numerator))}")
	else:
		return (f"{sign}{int(abs(numerator))}/{int(abs(denominator))}", number)

def reduce_print(numerator, denominator):
	(new_numerator, new_denominator) = reduce_fraction(int(numerator), int(denominator))
	print_fraction(new_numerator, new_denominator)
