# computorv1
This is the docker version, for the non-docker version go to [here](https://github.com/Friendy/computorv1/tree/master) or select the master branch in this repo.
This app displays the reduced form of a polinomial and finds its roots,
if its degree is 2 or less.

---

## Table of Contents

1. [About](#about)  
2. [Installation](#installation)  
3. [Usage](#usage)
4. [Other](#other) 

---

## About

The main part displays the reduced form, determines polinomial degree and finds the roots. The bonus part also displays the roots as an irreducable fraction and complex roots if applicable, shows input errors and intermediate steps.

---

## Installation

### Prerequisites

- Docker

### Steps

1. Clone the repository:  
   ```bash
   git clone https://github.com/Friendy/computorv1.git .
2. Build and run the docker container
   ```bash
   make all
---

## Usage

### Format
Term format: n * X^p, where n is the coefficient, X - the indeterminate, p - power

Coefficient: A coefficient is an integer or a float. It should have no leading zeros
except for a single zero before the float point, for example: 00.056 should be replaced
with 0.056

### Main part

```bash
python -m main.computor [polynomial]
```

### Bonus part

1. General usage
   ```bash
	python -m bonus.computor [polynomial]
2. For showing intermediate steps
   ```bash
	python -m bonus.computor [polynomial] steps
3. Help
   ```bash
	python -m bonus.computor h
### Tests

1. A bunch of tests for the main part
   ```bash
	./run-tests.sh
2. bonus tests
   ```bash
	./run-tests.sh bonus
3. bonus input error tests
   ```bash
	./run-tests.sh check
4. bonus intermediate steps tests
   ```bash
	./run-tests.sh steps
## Other
A tool to check the roots.

Solving quadratic equations online:
https://www.calculator.net/quadratic-formula-calculator.html
