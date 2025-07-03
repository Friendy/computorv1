#!/bin/bash

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source $DIR/func.sh
FILE_PATH="$DIR/../computor_bonus.py"

print_group_name "subject tests"
run_code "$FILE_PATH" "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
run_code "$FILE_PATH" "5 * X^0 + 4 * X^1 = 4 * X^0"
run_code "$FILE_PATH"  "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"

print_group_name "first negative test"
run_code "$FILE_PATH" "- 5 * X^0 - 4 * X^1 = 4 * X^0"
run_code "$FILE_PATH" "- 5 * X^0 - 4 * X^1 = - 4 * X^0"

print_group_name "fraction tests"
run_code "$FILE_PATH" "5 * X^0 + 4 * X^1 - 8 * X^2 = 1 * X^0"
run_code "$FILE_PATH" "5 * X^0 + 4 * X^1 - 15 * X^2 = 1 * X^0"
run_code "$FILE_PATH" "- 0.50 * X^0 + 4 * X^1 + 8 * X^2 = 1 * X^0"

print_group_name "d negative test"
run_code "$FILE_PATH" "- 1 * X^1 + 7 * X^2 = - 6 * X^0"
run_code "$FILE_PATH" "- 2 * X^1 - 43 * X^2 = 13 * X^0"

print_group_name "discriminant zero"
run_code "$FILE_PATH" "1 * X^2 + 2 * X^1 = - 1 * X^0"
run_code "$FILE_PATH" "2 * X^2 + 3 * X^1 = - 1.125 * X^0"

# echo "*****ZERO TESTS*******"
# input errors: sign check, check coef, check x power, input check