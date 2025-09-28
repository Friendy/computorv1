#!/bin/bash

if [[ $1 = "bonus" ]]
then
	bash tests/test_bonus.sh
elif [[ $1 = "check" ]]
then
	bash tests/checker.sh
elif [[ $1 = "steps" ]]
then
	bash tests/intermediate.sh
else
	bash tests/test.sh
fi
