#!/bin/bash

if [[ $1 = "bonus" ]]
then
	bash tests/test_bonus.sh
elif [[ $1 = "input" ]]
then
	bash tests/checker.sh
else
	bash tests/test.sh
fi
