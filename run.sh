#!/bin/bash

b=$(echo "bonus")
if [[ $1 = "bonus" ]]
then
	bash tests/test_bonus.sh
else
	bash tests/test.sh
fi
