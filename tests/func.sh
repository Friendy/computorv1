#!/bin/bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# FILE_PATH="$DIR/../computor.py"
# FILE_PATH_BONUS="$DIR/../computor_bonus.py"

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

run_code(){
	print_input "$2"
	if [[ $3 = "steps" ]]
	then
		python "$1" "$2" "$3"
	else
		python "$1" "$2"
	fi
}

# run_code_b(){
# 	print_input "$1"
# 	python "$FILE_PATH_BONUS" "$1"
# }