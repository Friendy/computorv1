import sys
from utils import reduction, print_reduced, solution, getDegree

# getting input
if len(sys.argv) > 1:
    input_data = sys.argv[1]
else:
    exit()

reduced_array = reduction(input_data)

# uncomment the next line if needed for debugging
# print("reduced array: ", reduced_array)

degree = getDegree(reduced_array)
print_reduced(reduced_array, degree)
print("Polynomial degree:", degree)
solution(reduced_array, degree)
