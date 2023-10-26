"""
chapter 1 Ex5
Write a Python program which accepts the radius of a circle 
from the user and compute the area.
"""
#In this program we will compute the area using radius of the cicle
from math import pi
r=float(input("Input the Radiusof the circle : "))
print("Area= ",pi*r**2)
"""
1.from math import pi: This line imports the mathematical constant pi from the Python math module. pi represents the mathematical value of π (pi), which is used in calculations related to circles.

2.r = float(input("Input the Radius of the circle: ")): This line prompts the user to input the radius of the circle. The input is captured as a string using the input() function and is then converted to a floating-point number (type float) using float(). This allows the user to input a decimal value for the radius.

3.print("Area =", pi * r**2): This line calculates the area of the circle using the formula for the area of a circle, which is π (pi) times the square of the radius (π * r^2). It then prints the result using print(), including the descriptive message "Area = " to make it clear what the output represents.
"""