import sys
from main.utils import reduction, print_reduced, getDegree, print_colored
from .utils import solution, reduce_fraction, print_help
from .checker import input_check
from .error import print_error
from main.operations import round6

# getting input
if len(sys.argv) > 1:
	input_data = sys.argv[1]
	if input_data == "h":
		print_help()
else:
	try:
		raise Exception("No or empty argument. Read README.md")
	except Exception as e:
		print_error(e, "", 3)
		exit(-1)
steps = False
if len(sys.argv) > 2 and sys.argv[2] == "steps":
	steps = True
input_check(input_data)

reduced_list = reduction(input_data)

degree = getDegree(reduced_list)
print_reduced(reduced_list, degree)
print_colored("Polynomial degree: ", "blue", "")
print_colored(f"{degree}", "green")
solution(reduced_list, degree, steps)