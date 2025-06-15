import sys
import utils
import math

# python computor.py "5.11 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
# python computor.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0" 

# input_data = ""

# getting input
if len(sys.argv) > 1:
    input_data = sys.argv[1]
else:
    exit

# initializing an array where the reduced data will be   
# the form: coefficient[power]
reduced_array = []

# finding positions of the equal sign and the end
last_ind = len(input_data) - 1
eq_ind = input_data.find('=')

# reducing the left and the right side of the equation
utils.reduction(input_data, reduced_array, 0, eq_ind)
utils.reduction(input_data, reduced_array, eq_ind, last_ind)
print("arr: ", reduced_array)
degree = len(reduced_array) - 1
utils.print_reduced(reduced_array, degree)
print("Polynomial degree:", degree)
utils.solution(reduced_array, degree)
# print(utils.pow2(6.4))
# n = sys.float_info.min
# print(sys.maxsize)
# print(n)
# print("math:", math.sqrt(n))
# print("my:", utils.square_root(n))



# utils.solution(reduced_array, degree)
# utils.printk()
# print(utils.get_coef("r - 5.9 * y", 10))
# print(input_data.rfind(' ', 0, 10))
# print('\n')
# print(input_data)