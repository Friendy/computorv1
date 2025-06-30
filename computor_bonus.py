import sys
from utils import reduction, print_reduced, getDegree
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
# input_check(input_data)
# exit(-1)
reduced_array = reduction(input_data)

# uncomment the next line if needed for debugging
# print("reduced array: ", reduced_array)

degree = getDegree(reduced_array)
print_reduced(reduced_array, degree)
print("Polynomial degree:", degree)
solution(reduced_array, degree, steps)
