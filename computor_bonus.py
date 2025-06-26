import sys
from utils import reduction, print_reduced, solution, getDegree
from utils_bonus import input_check

# getting input
if len(sys.argv) > 1:
    input_data = sys.argv[1]
else:
    try:
        raise Exception("No or empty argument")
    except Exception as e:
        print(f"Error: {e}")
        exit(-1)
input_check(input_data)
print('\x1b[6;30;41m' + 'Success!' + '\x1b[0m')
exit(-1)
reduced_array = reduction(input_data)

# uncomment the next line if needed for debugging
# print("reduced array: ", reduced_array)

degree = getDegree(reduced_array)
print_reduced(reduced_array, degree)
print("Polynomial degree:", degree)
solution(reduced_array, degree)
