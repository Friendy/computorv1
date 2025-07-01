import sys
from utils import reduction, print_reduced, getDegree, print_colored
from utils_bonus import solution, reduce_fraction
from checker import input_check

# getting input
if len(sys.argv) > 1:
    input_data = sys.argv[1]
else:
    try:
        raise Exception("No or empty argument")
    except Exception as e:
        print(f"Error: {e}")
        exit(-1)
steps = False
if len(sys.argv) > 2 and sys.argv[2] == "steps":
    steps = True
input_check(input_data)

# exit(-1)
reduced_list = reduction(input_data)

# uncomment the next line if needed for debugging
# print("reduced list: ", reduced_list)

degree = getDegree(reduced_list)
print_reduced(reduced_list, degree)
print_colored("Polynomial degree: ", "blue", "")
print_colored(f"{degree}", "green")
solution(reduced_list, degree, steps)
