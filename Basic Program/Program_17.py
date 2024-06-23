'''
WAP to take the radius from the user and calculate its
perimeter = 2*pi^r and area of the circle = pi*r^2
'''
import math as m
r = int(input("enter radius :- " ))
perimeter = 2 * m.pi*r
print(f"perimeter of circle :- {perimeter} ")
area = m.pi*r*r
print(f"Area of circle:- {area}")