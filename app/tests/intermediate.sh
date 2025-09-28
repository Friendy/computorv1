#!/bin/bash

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE="bonus.computor"
source $DIR/func.sh

print_group_name "discriminant positive"
run_code "$MODULE" "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0" "steps"
run_code "$MODULE" "- 0.50 * X^0 + 4 * X^1 + 8 * X^2 = 1 * X^0" "steps"
run_code "$MODULE" "7 * X^2 = - 6 * X^1" "steps"
run_code "$MODULE" "7 * X^2 = - 14 * X^1" "steps"
run_code "$MODULE" "- 1.5 * X^1 + 1 * X^2 = - 0.5 * X^0" "steps"
run_code "$MODULE" "- 0.375 * X^1 + 1 * X^2 = - 0.01389 * X^0" "steps"

print_group_name "negative discriminant"
run_code "$MODULE" "- 1 * X^1 + 7 * X^2 = - 6 * X^0" "steps"

print_group_name "degree 1"
run_code "$MODULE" "5 * X^0 + 4 * X^1 = 4 * X^0" "steps"
run_code "$MODULE" "6 * X^0 + 4 * X^1 = 4 * X^0" "steps"

print_group_name "discriminant zero"
run_code "$MODULE" "1 * X^2 + 2 * X^1 = - 1 * X^0" steps
run_code "$MODULE" "2 * X^2 + 3 * X^1 = - 1.125 * X^0" steps
run_code "$MODULE" "1 * X^2 + 8 * X^1 = - 16 * X^0" steps




# echo "*****ZERO TESTS*******"
# input errors: sign check, check coef, check x power, input check