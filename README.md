# computorv1

*********************************
*		Mandatory Part			*
*********************************

	To run from the root folder:
python -m main.computor "some polynomial"
	Tests:
./run.sh
*****************************
*		Bonus Part			*
*****************************
	To run from the root folder:
python -m bonus.computor "some polynomial"
	For showing intermediate steps:
python -m bonus.computor "some polynomial" steps
	For help:
python -m bonus.computor h
	Tests:
./run.sh check  -  bonus, input error tests
./run.sh bonus -  bonus tests
./run.sh steps -  bonus intermediate steps tests


python -m bonus.computor "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0" steps
Solving quadratic equations online
https://www.calculator.net/quadratic-formula-calculator.html