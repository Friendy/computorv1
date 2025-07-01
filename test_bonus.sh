#!/bin/bash
print_input(){
	echo -e "\033[0;33mInput:\033[0m" "\033[0;33m$1\033[0m"
}

print_group_name(){
upper=$(echo -e "$1" | tr "[:lower:]" "[:upper:]")
len=$(echo $1 | wc -c)
padding1=$(( (29 - $len) / 2 ))
padding2=$((28 - $padding1))
format=$(echo "%0s %"$padding2"s %"$padding1"s\n")
echo -e "\033[0;32m*******************************\033[0m"
name=$(printf "$format" "*" "$upper" "*")
echo -e "\033[0;32m$name\033[0m"
echo -e "\033[0;32m*******************************\033[0m"
}

print_group_name "subject tests"

print_input "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
python computor_bonus.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
print_input "5 * X^0 + 4 * X^1 = 4 * X^0"
python computor_bonus.py "5 * X^0 + 4 * X^1 = 4 * X^0"
print_input "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
python computor_bonus.py  "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"

print_group_name "first negative test"
print_input "- 5 * X^0 - 4 * X^1 = 4 * X^0"
python computor_bonus.py "- 5 * X^0 - 4 * X^1 = 4 * X^0"
print_group_name "zero tests"
print_input "1 * X^0 - 0 * X^1 = 0 * X^0"
python computor_bonus.py "1 * X^0 - 0 * X^1 = 0 * X^0"
print_input "0 * X^0 - 0 * X^1 = 0 * X^0"
python computor_bonus.py "0 * X^0 - 0 * X^1 = 0 * X^0"
print_group_name "fraction tests"
print_input "5 * X^0 + 4 * X^1 - 8 * X^2 = 1 * X^0"
python computor_bonus.py "5 * X^0 + 4 * X^1 - 8 * X^2 = 1 * X^0"
print_input "5 * X^0 + 4 * X^1 - 15 * X^2 = 1 * X^0"
python computor_bonus.py "5 * X^0 + 4 * X^1 - 15 * X^2 = 1 * X^0"

print_group_name "d negative test"
print_input "- 1 * X^1 + 7 * X^2 = 6 * X^0"
python3 computor_bonus.py "- 1 * X^1 - 7 * X^2 = 6 * X^0"
# echo "*****ZERO TESTS*******"
# input errors: sign check, check coef, check x power, input check