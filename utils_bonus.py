import re, sys
from utils import pow2, square_root, round6
# from utils_bonus import reduce_fraction

def print_select(start, selection, end):
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
		print(f"{sign}{int(abs(numerator))}")
	else:
	    print(f"{sign}{int(abs(numerator))}/{int(abs(denominator))} ({number})")
	
def solution(arr, degree, steps):
	if degree == 2:
		D_term1 = pow2(arr[1])
		D_term2 = - 4*arr[2]*arr[0]
		D = D_term1 + D_term2
		if steps == True:
			sign = '+'
			if D_term2 < 0:
				sign = "-"
			print(f"Discriminant: D = b^2 - 4ac = {arr[1]}^2 {sign} 4 * {abs(arr[2])} * {abs(arr[0])} = {round6(D)}")
		if D > 0:
			D_root = square_root(D)
			# print(f"Discriminant: {round6(D)}")
			if abs(D_root - int(D_root)) == 0: #fraction format
				numerator1 = int(-arr[1] + D_root)
				numerator2 = int(-arr[1] - D_root)
				denominator = int(2*arr[2])
				print("Discriminant is strictly positive, the two solutions are:")
				(new_numerator, new_denominator) = reduce_fraction(numerator1, denominator)
				print_fraction(new_numerator, new_denominator)
				(new_numerator, new_denominator) = reduce_fraction(numerator2, denominator)
				print_fraction(new_numerator, new_denominator)
			else:
				s1 = (-arr[1] + D_root)/(2*arr[2])
				s2 = (-arr[1] - D_root)/(2*arr[2])
				print("Discriminant is strictly positive, the two solutions are:", round6(s1), round6(s2), sep="\n")
		elif D == 0:
			print("Discriminant equals zero, the solution is:", round6(-arr[1]/2*arr[2]))
			print(f"Fraction format:")
			reduce_fraction(-arr[1], 2*arr[2])
		else:
			print("Discriminant is strictly negative, there is no real solution:")
			D_root = square_root(-D)
			# print("root", round6(D_root))
			real = round6(-arr[1]/(2*arr[2]))
			im = round6(D_root/(2*arr[2]))
			print(f"Complex solutions:\n{real} + i * {im}\n{real} - i * {im}")
	elif degree == 1:
		print("The solution is:", -arr[0]/arr[1], sep="\n")
	elif degree == 0:
		if (arr[0] == 0):
			print("Any real number is a solution")
			reduce_fraction(-arr[1], 2*arr[2])
		else:
			print("This equation has no solutions")
	else:
		print("The polynomial degree is strictly greater than 2, I can't solve.")