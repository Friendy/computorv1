#!/bin/bash
echo "*****SUBJECT TEST*******"
python computor_bonus.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
python computor_bonus.py "5 * X^0 + 4 * X^1 = 4 * X^0"
python computor_bonus.py  "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"

echo "*****FIRST NEGATIVE TEST*******"
python computor_bonus.py "- 5 * X^0 - 4 * X^1 = 4 * X^0"
echo "*****ZERO TESTS*******"
python computor_bonus.py "1 * X^0 - 0 * X^1 = 0 * X^0"
python computor_bonus.py "0 * X^0 - 0 * X^1 = 0 * X^0"
echo "*****FRACTION TESTS*******"
python computor_bonus.py "5 * X^0 + 4 * X^1 - 8 * X^2 = 1 * X^0"
python computor_bonus.py "5 * X^0 + 4 * X^1 - 15 * X^2 = 1 * X^0"
# echo "*****ZERO TESTS*******"
# input errors: sign check, check coef, check x power, input check