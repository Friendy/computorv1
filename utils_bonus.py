import re, sys
from utils import pow2, square_root, round6, print_colored, print_solution, Solutions
# from utils_bonus import reduce_fraction

def print_select(start, selection, end):
	if selection:
		print(f"{start}{'\x1b[6;30;41m'}{selection}{'\x1b[0m'}{end}")

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

def solution(list, degree, steps):
	if degree == 2:
		D_term1 = pow2(list[1])
		D_term2 = - 4*list[2]*list[0]
		D = D_term1 + D_term2
		if steps == True:
			sign = '+'
			if D_term2 < 0:
				sign = "-"
			print(f"Discriminant: D = b^2 - 4ac = {list[1]}^2 {sign} 4 * {abs(list[2])} * {abs(list[0])} = {round6(D)}")
		if D > 0:
			D_root = square_root(D)
			# print(f"Discriminant: {round6(D)}")
			if abs(D_root - int(D_root)) == 0: #fraction format
				print_colored("Discriminant is strictly positive, the two solutions are:", "blue")
				reduce_print(-list[1] + D_root, 2*list[2])
				reduce_print(-list[1] - D_root, 2*list[2])
			else:
				print_solution(Solutions.POSITIVE, ((-list[1] + D_root)/(2*list[2]), (-list[1] - D_root)/(2*list[2])))
		elif D == 0:
			(numerator, denominator) = reduce_fraction(-list[1], 2*list[2])
			print(f"Discriminant equals zero, the solution is: {print_fraction(numerator, denominator)}")
		else:
			print_colored("Discriminant is strictly negative, there is no real solution:", "blue")
			D_root = square_root(-D)
			# print("root", round6(D_root))
			real = round6(-list[1]/(2*list[2]))
			im = round6(D_root/(2*list[2]))
			print_colored("Complex solutions:", "blue")
			print_colored(f"{real} + i * {im}\n{real} - i * {im}","green")
			# print(f"Complex solutions:\n{real} + i * {im}\n{real} - i * {im}")
	elif degree == 1:
		(numerator, denominator) = reduce_fraction(-list[0],list[1])
		print_colored(f"The solution is: ","blue")
		print_fraction(numerator, denominator)
		# reduce_fraction(-list[0],list[1])
	elif degree == 0:
		if (list[0] == 0):
			print("Any real number is a solution")
		else:
			print("This equation has no solutions")
	else:
		print("The polynomial degree is strictly greater than 2, I can't solve.")