#!/bin/bash

if [[ $1 = "bonus" ]]
then
	bash app/tests/test_bonus.sh
elif [[ $1 = "check" ]]
then
	bash app/tests/checker.sh
elif [[ $1 = "steps" ]]
then
	bash app/tests/intermediate.sh
else
	bash app/tests/test.sh
fi
