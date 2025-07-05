
from enum import IntEnum
from main.utils import pow2, square_root, round6, print_colored, print_solution
from main.utils import Solutions as SolutionsMain
from .steps import print_solution_steps
from .fractions import reduce_fraction, print_fraction, reduce_print
from .utils import is_interesting, Solutions


def solution(list, degree, steps):
	if degree == 2:
		D_term1 = pow2(list[1])
		D_term2 = - 4*list[2]*list[0]
		D = D_term1 + D_term2
		if steps:
			sign = '+'
			if D_term2 < 0:
				sign = "-"
			print_colored(f"Notation: ax^2 + bx + c = 0\nDiscriminant: ", "purple", endline="")
			print_colored(f"D = b^2 - 4ac = {list[1]}^2 {sign} 4 * {abs(list[2])} * {abs(list[0])} = {D_term1} {sign} {abs(D_term2)} = {round6(D)}", "purple")
		if D > 0:
			D_root = square_root(D)
			if steps:
				print_solution_steps(Solutions.POSITIVE1, list, D_root)
				print_solution_steps(Solutions.POSITIVE2, list, D_root)
			elif is_interesting(D_root, list[1]):
				print_colored("Discriminant is strictly positive, the two solutions are:", "blue")
				reduce_print(-list[1] + D_root, 2*list[2])
				reduce_print(-list[1] - D_root, 2*list[2])
			else:
				print_solution(SolutionsMain.POSITIVE, ((-list[1] + D_root)/(2*list[2]), (-list[1] - D_root)/(2*list[2])))
		elif D == 0:
			if steps:
				print_solution_steps(Solutions.ZERO, list, 0)
			else:
				print_colored(f"Discriminant equals zero, the solution is: ","blue")
				(numerator, denominator) = reduce_fraction(-list[1], 2*list[2])
				print_fraction(numerator,denominator)
		else:
			print_colored("Discriminant is strictly negative, there is no real solution:", "blue")
			D_root = square_root(-D)
			real = round6(-list[1]/(2*list[2]))
			im = round6(D_root/(2*list[2]))
			print_colored("Complex solutions:", "blue")
			print_colored(f"{real} + i * {abs(im)}\n{real} - i * {abs(im)}","green")
			# print(f"Complex solutions:\n{real} + i * {im}\n{real} - i * {im}")
	elif degree == 1:
		if steps:
			print_solution_steps(Solutions.DEGREE1, list, 0)
		else:
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