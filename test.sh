#!/bin/bash
echo "*****SUBJECT TEST*******"
python3 computor.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
python3 computor.py "5 * X^0 + 4 * X^1 = 4 * X^0"
python3 computor.py  "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"

echo "*****FIRST NEGATIVE TEST*******"
python3 computor.py "- 5 * X^0 - 4 * X^1 = 4 * X^0"
echo "*****ZERO TESTS*******"
python3 computor.py "1 * X^0 - 0 * X^1 = 0 * X^0"
python3 computor.py "0 * X^0 - 0 * X^1 = 0 * X^0"