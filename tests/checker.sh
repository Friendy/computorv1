#!/bin/bash

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE="bonus.computor"
source $DIR/func.sh

print_group_name "space missing tests"
run_code "$MODULE"  "5 * X^0 +4 * X^1 - 8 * X^2 = 1 * X^0"
run_code "$MODULE" "5 * X^0 + 4 * X^1 - 15 * X^2= 1 * X^0"
run_code "$MODULE" "-5 * X^0 + 4 * X^1 - 15 * X^2 = 1 * X^0"
run_code "$MODULE" "5 * X^0 + 4* X^1 - 15 * X^2 = 1 * X^0"
run_code "$MODULE" "5 * X^0 + 4 * X^1 - 15 * X^2 = 1 *X^0"
run_code "$MODULE" "- 5 * X^0 + 4 * X^1 - 15 * X^2 =1 * X^0"
run_code "$MODULE" "- 5 * X^0+ 4 * X^1 - 15 * X^2 = 1 * X^0"

print_group_name "term missing tests"
run_code "$MODULE" "5 * X^0 + 4 * X^1 - 15 * X^2 ="
run_code "$MODULE" "5 * X^0 + 4 * X^1 - 15 * X^2 =  "
run_code "$MODULE" "5 * X^0 + 4 * X^1 = - 15 * X^2 + "
run_code "$MODULE" "5 * X^0 + 4 * X^1 = - 15 * X^2 +"

print_group_name "first sign tests"
run_code "$MODULE" "-5 * X^0 + 4 * X^1 * 8 * X^2 = 1 * X^0"
run_code "$MODULE" "- 5 * X^0 + 4 * X^1 - 8 * X^2 = -1 * X^0"
run_code "$MODULE" "^5 * X^0 + 4 * X^1 - 8 * X^2 = -1 * X^0"

print_group_name "wrong sign tests"
run_code "$MODULE" "5 * X^0 + 4 * X^1 ^ 8 * X^2 = 1 * X^0"
run_code "$MODULE" "5 * X^0 + 4 * X^1 - 8 ^ X^2 = 1 * X^0"

print_group_name "indeterminate"
run_code "$MODULE" "5 * X^0 + 4 * 42^1 - 8 * X^2 = 1 * X^0"
run_code "$MODULE" "42^1 - 8 * X^2 = 1 * X^0"
run_code "$MODULE" "5 * X^ 0 + 4 * X^1 - 15 * X^2 = 1 * X^0"

print_group_name "forbidden symbols"
run_code "$MODULE" "tet  tereyrywey=eyeyewyerwy"
run_code "$MODULE" "tet  tereyryweyeyeyewy77erwy"
run_code "$MODULE" "5 * X^0 + t * X^1 - 8 * X^2 = 1 * X^0"
run_code "$MODULE" "^66 = 44"

print_group_name "coefficent format"
run_code "$MODULE" "- 05 * X^0 + 4 * X^1 + 8 * X^2 = 1 * X^0"
run_code "$MODULE" "- 5^ * X^0 + 4 * X^1 + 8 * X^2 = 1 * X^0"
run_code "$MODULE" "- 5. * X^0 + 4 * X^1 + 8 * X^2 = 1 * X^0"


# echo "*****ZERO TESTS*******"
# input errors: sign check, check coef, check x power, input check