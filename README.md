# computorv1
This is the docker version, for the non-docker version go to
This app displays the reduced form of a polinomial and finds its roots,
if its degree is 2 or less.

---

## Table of Contents

1. [About](#about)  
2. [Features](#features)  
3. [Installation](#installation)  
4. [Usage](#usage)  

---

## About

The main part displays the reduced form, determines polinomial degree and finds the roots. The bonus part also displays the roots as an irreducable fraction and complex roots if applicable, shows input errors and intermediate steps.

---

## Features

- Feature 1: brief explanation  
- Feature 2: brief explanation  
- Feature 3: brief explanation  

---

## Installation

### Prerequisites

- Docker (depending on your project)  

### Steps

1. Clone the repository:  
   ```bash
   git clone https://github.com/Friendy/computorv1.git .
2. Build and run the docker container
   make all
3. Build and run the docker container
   make all

## Usage

### Main part

python -m main.computor "a polynomial in a special format(#format)"

### Bonus part

1. General usage
	python -m bonus.computor "a polynomial in a special format(#format)"
2. For showing intermediate steps
	python -m bonus.computor "a polynomial in a special format(#format)" steps
3. Help
	python -m bonus.computor h

### Tests

./run-tests.sh - a bunch of tests for the main part

./run-tests.sh check  -  bonus, input error tests
./run-tests.sh bonus -  bonus tests
./run-tests.sh steps -  bonus intermediate steps tests

## Format
Term format: n * X^p, where n is the coefficient, X - the indeterminate, p - power
Coefficient: A coefficient is an integer or a float. It should have no leading zeros
except for a single zero before the float point, for example: 00.056 should be replaced
with 0.056


Solving quadratic equations online:
https://www.calculator.net/quadratic-formula-calculator.html