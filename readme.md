# Project Install Instructions

# Install

1. clone
2. pip install faker
3. pip install -r requirements.txt

# Testing

1. pytest
2. pytest --num_records=10
3. pytest --pylint --cov


# Implementation Steps

<<<<<<< HEAD
# Running the calculator via CLI   ( main.py )

python main.py  <number 1> <number 2> <operation>

# Example:

python3 main.py 5 3 add

# Output:

The result of 5 and 3 is equal to 8


# Command Pattern Calculator  ( dynamic_main.py )

## Overview
This project implements a **command-line calculator** using the **Command Pattern** and **Plugin Architecture**.
It supports dynamic command loading, unit testing, and exception handling.

## 🚀 Features
- Interactive REPL-based calculator
- **Command Pattern** for modularity
- **Plugin System** for dynamic command loading
- Supports `add`, `subtract`, `multiply`, `divide`
- **100% test coverage** with `pytest`

=======
1. Basic Calculator (Main Branch)

	Implement basic arithmetic functions (add, subtract, multiply, divide).
	
	Write unit tests for each function.

2. Intermediate Calculator (Part 2)

	Introduce Calculation class (instance methods).
	
	Implement static methods in Calculator class.
	
	Ensure exception handling for division by zero.
	
	Write additional unit tests.

3. Advanced Calculator (Part 3)

	Implement Calculations class (class methods) for history management.
	
	Use @classmethod, @staticmethod, and @property appropriately.
	
	Implement pytest fixtures and parameterized tests.
	
	Achieve 100% test coverage and pylint compliance.

4. Branching Strategy

	Main Branch: Basic Calculator (Functions Only).
	
	Part 2 Branch: OOP with Static Methods & Instance Methods.
	
	Part 3 Branch: Fully Featured Calculator (Class Methods, History, Parameterized Tests).


>>>>>>> main
