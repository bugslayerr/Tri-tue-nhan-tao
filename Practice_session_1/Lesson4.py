#!/usr/bin/env python3

"""Lesson 4: Program to calculate and display the sum of odd natural numbers from 1 to 100."""

count = int(0)
for i in range(0, 101):
	if i % 2 != 0:
		count+=i
print(f"sum of odd natural numbers from 1 to 100 is {count}")