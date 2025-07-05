# computorv1

*****************************************
*		Create Virtual Environment		*
*****************************************
brew install python - if python3 is not installed on mac
python3 -m venv .venv
source .venv/bin/activate

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


Solving quadratic equations online
https://www.calculator.net/quadratic-formula-calculator.html