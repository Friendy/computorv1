import re, sys
from enum import IntEnum
from utils import pow2, square_root, round6, print_colored, print_solution
from utils import Solutions as Solutions1
class Solutions(IntEnum):
	ZERO = 0
	POSITIVE1 = 1
	POSITIVE2 = 2
	NEGATIVE = -1
	POWER1 = 3

def print_select(start, selection, end):
	if selection:
		print(f"{start}{'\x1b[6;30;41m'}{selection}{'\x1b[0m'}{end}")

def print_help():
	coef_format = "A coefficient is an integer or a float. It should have no leading zeros\nexcept for a single zero before the float point, for example: 00.056 should be replaced\nwith 0.056"
	print_colored("HELP:", "brown")
	print_colored("Term format: ", "purple", endline="")
	print_colored("n * X^p, where n is the coefficient, X - the indeterminate, p - power", "blue")
	print_colored("Coefficient: ", "purple", endline="")
	print_colored(coef_format, "blue")
	exit()

def isdenominator(candidate, n):
	r = n/candidate
	return abs((r) - int(r)) == 0

def reduce_fraction(numerator, denominator):
	# print(f" start {numerator}, {denominator}")
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
	# print(f" reduce {numerator}, {denominator}")
	return (numerator, denominator)

def print_fraction(numerator, denominator):
	number = round6(numerator/denominator)
	sign = ""
	if number < 0:
		sign = "-"
	if abs(denominator) == 1:
		print_colored(f"{sign}{int(abs(numerator))}", "green")
	else:
		print_colored(f"{sign}{int(abs(numerator))}/{int(abs(denominator))} ({number})", "green")

def reduce_print(numerator, denominator):
	(new_numerator, new_denominator) = reduce_fraction(int(numerator), int(denominator))
	print_fraction(new_numerator, new_denominator)

# def print_solution_steps(type, list, D_root):
# 	match type:
# 		case Solutions.POSITIVE1:
# 			text = "Discriminant is strictly positive, the two solutions are:"
# 		case Solutions.POSITIVE2:
# 			text = "h"
# 		case Solutions.ZERO:
# 			text = "Discriminant equals zero, the solution is:"
# 		case Solutions.POWER1:
# 			text = "The solution is:"
# 		case Solutions.NEGATIVE:
# 			text = "FDg"
# 	print_colored(text, "blue")


def print_solution_steps(type, list, D_root):
	text=""
	match type:
		case Solutions.POSITIVE1:
			text = "Discriminant is strictly positive, the two solutions are:"
			sign = "+"
			numerator = round6(-list[1] + D_root)
		case Solutions.POSITIVE2:
			# text = ""
			sign = "-"
			numerator = round6(-list[1] - D_root)
		case Solutions.ZERO:
			text = "Discriminant equals zero, the solution is:"
		case Solutions.POWER1:
			text = "The solution is:"
		case Solutions.NEGATIVE:
			text = ""
	if text:
		print_colored(text, "blue")
	if type == Solutions.POSITIVE1 or type == Solutions.POSITIVE2:
		step1 = f"({round6(-list[1])} {sign} {(round6(D_root))})/(2 * {round6(list[2])})"
		step2 = f"{numerator}/{round6(2*list[2])}"
		step3 = f"{round6(numerator/round6(2*list[2]))}"
		print_colored(f'-b {sign} \u221AD/2a = {step1} = {step2} = {step3}', "purple")


# match type:
# 	case 1:
# 		text = "text1"
# 	case 2:
# 		text = "text2"
# print(text)

def solution(list, degree, steps):
	if degree == 2:
		D_term1 = pow2(list[1])
		D_term2 = - 4*list[2]*list[0]
		D = D_term1 + D_term2
		if steps:
			sign = '+'
			if D_term2 < 0:
				sign = "-"
			print_colored(f"Discriminant: ", "purple", endline="")
			print_colored(f"D = b^2 - 4ac = {list[1]}^2 {sign} 4 * {abs(list[2])} * {abs(list[0])} = {D_term1} + {D_term2}  = {round6(D)}", "purple")
		if D > 0:
			D_root = square_root(D)
			# print(f"Discriminant: {round6(D)}")
			if abs(D_root - int(D_root)) == 0: #fraction format
				print_colored("Discriminant is strictly positive, the two solutions are:", "blue")
				reduce_print(-list[1] + D_root, 2*list[2])
				reduce_print(-list[1] - D_root, 2*list[2])
			else:
				if steps:
					print_solution_steps(Solutions.POSITIVE1, list, D_root)
					print_solution_steps(Solutions.POSITIVE2, list, D_root)
				else:
					print_solution(Solutions1.POSITIVE, ((-list[1] + D_root)/(2*list[2]), (-list[1] - D_root)/(2*list[2])))
		elif D == 0:
			(numerator, denominator) = reduce_fraction(-list[1], 2*list[2])
			print(numerator/denominator)
			print_solution(Solutions1.ZERO, (numerator/denominator))
		else:
			print_colored("Discriminant is strictly negative, there is no real solution:", "blue")
			D_root = square_root(-D)
			# print("root", round6(D_root))
			real = round6(-list[1]/(2*list[2]))
			im = round6(D_root/(2*list[2]))
			print_colored("Complex solutions:", "blue")
			print_colored(f"{real} + i * {abs(im)}\n{real} - i * {abs(im)}","green")
			# print(f"Complex solutions:\n{real} + i * {im}\n{real} - i * {im}")
	elif degree == 1:
		(numerator, denominator) = reduce_fraction(-list[0],list[1])
		print_colored(f"The solution is: ","blue")
		print_fraction(numerator, denominator)
	elif degree == 0:
		if (list[0] == 0):
			print_colored("Any real number is a solution", "blue")
		else:
			print_colored("This equation has no solutions", "blue")
	else:
		print_colored("The polynomial degree is strictly greater than 2, I can't solve.", "blue")