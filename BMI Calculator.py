# -*- coding: utf-8 -*-
# """
# Created on Sun Sep 17 01:17:45 2023

# @author: talha.i
# """

# BMI Calculator 1

height = input('Enter your height in m: ')

weight = input('Enter your weight in kg: ')

#SOLUTION 1 :
height_square = float(height) ** 2

int_weight = int(weight)

bmi = int(int_weight / height_square)

print(bmi)

# SOLUTION 2 :
bmi = int(weight) / float(height) ** 2

print(int(bmi))