"""
File: quadratic_solver.py
Name:
-----------------------
This program implements a console-based solver for a
quadratic equation.

It asks the user to input three values a, b, and c,
and computes the roots of the equation:
ax^2 + bx + c = 0.

The output format should match the sample run shown
in the Assignment 2 handout.
"""

import math

def main():
	print("stanCode Quadratic Solver!")
	a = int(input("Please enter a: "))
	b = int(input("Please enter b: "))
	c = int(input("Please enter c: "))
	d = b*b-4*a*c

	if d == 0:
		e = math.sqrt(d)
		root = (-b+e)/(2*a)
		print("One root: " + str(root))

	if d > 0:
		e = math.sqrt(d)
		root_1 =(-b+e)/(2*a)
		root_2 =(-b-e)/(2*a)
		print("Two roots: " + str(root_1) +"," + str(root_2))

	if d < 0:
		print("No real roots")

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
