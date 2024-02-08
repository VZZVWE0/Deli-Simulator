# Created by Anna Felipe on April 28 2016
# Exercise 11 - Addition, Multiplication and Finds the Average of Five
# Lab 10
# File name: Ex11Lab10.py
# D2L File Name: Ex11Lab10.py.txt.

# Screen Prompt to User
print('FLYING TIGERS DELI')
print('===================')
print()
print('Welcome to our online ordering system.')
print('Instructions:')
print('Type your Sandwich Order and Cost')
print()
print('If you DO NOT want  Sandwich')
print('Please Type => NONE and the Cost as 0 - Thank You')
print()

orderOne = input('Order #1 - What type of Sandwich? => ')
costOne = float(input('Order #1 - Cost of Sandwich? => '))
print()
orderTwo = input('Order #2 - What type of Sandwich? => ')
costTwo = float(input('Order #2 - Cost of Sandwich? => '))
print()
orderThree = input('Order #3 - What type of Sandwich? => ')
costThree = float(input('Order #3 - Cost of Sandwich? => '))
print()

# Calculate and Output Results - prime total to zero
costSum = 0
costSum = costOne + costTwo + costThree

print('Here is Your Order:')

if orderOne.lower() != 'none':
	print(orderOne, costOne)
	
if orderTwo.lower() != 'none':
	print(orderTwo, costTwo)
	
if orderThree.lower() != 'none':
	print(orderThree, costThree)
	
print('Total Cost = ', costSum)
print()


# End of File