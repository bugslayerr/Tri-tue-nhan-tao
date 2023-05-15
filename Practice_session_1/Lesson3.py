#!/usr/bin/env python3

"""Program to solve first-order equations ax + b = 0, where a, b are the real coefficients entered from the keyboard."""
try:
	a = int(input("Enter a: "))
	b = int(input("Enter b: "))
	result = -b/a
	print(f"x = -b/a => x = {-b/a}")
except ZeroDivisionError:
	print("number a have to differ 0")