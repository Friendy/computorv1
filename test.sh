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
python3 computor.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"

print_input "5 * X^0 + 4 * X^1 = 4 * X^0"
python3 computor.py "5 * X^0 + 4 * X^1 = 4 * X^0"

print_input "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
python3 computor.py  "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"

print_group_name "first negative"
print_input "- 5 * X^0 - 4 * X^1 = 4 * X^0"
python3 computor.py "- 5 * X^0 - 4 * X^1 = 4 * X^0"

print_group_name "zero tests"
print_input "1 * X^0 - 0 * X^1 = 0 * X^0"
python3 computor.py "1 * X^0 - 0 * X^1 = 0 * X^0"
print_input "0 * X^0 - 0 * X^1 = 0 * X^0"
python3 computor.py "0 * X^0 - 0 * X^1 = 0 * X^0"
print_input "0 * X^0 - 1 * X^1 = 0 * X^0"
python3 computor.py "0 * X^0 - 1 * X^1 = 0 * X^0"

print_group_name "integer solutions tests"
print_input "- 1 * X^1 + 1 * X^2 = 6 * X^0"
python3 computor.py "- 1 * X^1 + 1 * X^2 = 6 * X^0"
print_input computor.py "- 2 * X^1 = 648 * X^0"
python3 computor.py "- 2 * X^1 = 648 * X^0"

print_group_name "float point tests"
print_input "- 34.07 * X^1 + 4.973 * X^2 = 12 * X^0"
python3 computor.py "- 34.07 * X^1 + 4.973 * X^2 = 12 * X^0"
print_input computor.py "- 256.705 * X^1 = 7845 * X^0"
python3 computor.py "- 256.705 * X^1 = 7845 * X^0"

print_group_name "zero degree tests"
print_input "5 * X^0 = 1 * X^0 + 4 * X^0"
python3 computor.py "5 * X^0 = 1 * X^0 + 4 * X^0"
print_input "43 * X^0 = 1 * X^0"
python3 computor.py "43 * X^0 = 1 * X^0"

print_group_name "degree over 2 tests"
print_input "- 46 * X^1 + 83 * X^10 - 7 * X^3 = 3 * X^0 + 7 * X^10"
python3 computor.py  "- 46 * X^1 + 83 * X^10 - 7 * X^3 = 3 * X^0 + 7 * X^10"
print_input "- 53 * X^5 = 7 * X^25"
python3 computor.py  "- 53 * X^5 = 7 * X^25"

print_group_name "other tests"
print_input "- 46 * X^1 + 83 * X^3 - 7 * X^2 = 83 * X^3"
python3 computor.py  "- 46 * X^1 + 83 * X^3 - 7 * X^2 = 83 * X^3"
print_input "- 53 * X^2 = 7 * X^1 - 6 * X^0"
python3 computor.py  "- 53 * X^2 = 7 * X^1 - 6 * X^0"



# input errors: sign check, check coef, check x power, input check