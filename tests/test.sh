#!/bin/bash

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source $DIR/func.sh

print_group_name "subject tests"
run_code "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
run_code "5 * X^0 + 4 * X^1 = 4 * X^0"
run_code "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"

print_group_name "first negative"
run_code "- 5 * X^0 - 4 * X^1 = 4 * X^0"

print_group_name "zero tests"
run_code "1 * X^0 - 0 * X^1 = 0 * X^0"
run_code "0 * X^0 - 0 * X^1 = 0 * X^0"
run_code "0 * X^0 - 1 * X^1 = 0 * X^0"

print_group_name "integer solutions tests"
run_code "- 1 * X^1 + 1 * X^2 = 6 * X^0"
run_code "- 2 * X^1 = 648 * X^0"

print_group_name "float point tests"
run_code "- 34.07 * X^1 + 4.973 * X^2 = 12 * X^0"
run_code "- 256.705 * X^1 = 7845 * X^0"

print_group_name "zero degree tests"
run_code "5 * X^0 = 1 * X^0 + 4 * X^0"
run_code "43 * X^0 = 1 * X^0"

print_group_name "degree over 2 tests"
run_code "- 46 * X^1 + 83 * X^10 - 7 * X^3 = 3 * X^0 + 7 * X^10"
run_code "- 53 * X^5 = 7 * X^25"

print_group_name "other tests"
run_code "- 46 * X^1 + 83 * X^3 - 7 * X^2 = 83 * X^3"
run_code "- 53 * X^2 = 7 * X^1 - 6 * X^0"
run_code "- 1 * X^1 = - 1 * X^2 + 6 * X^0"




# input errors: sign check, check coef, check x power, input check