"""
Description: https://algorithms.tutorialhorizon.com/colorful-numbers/

Objective: Given a number, find out whether its colorful or not.

Colorful Number: When in a given number, product of every digit of a sub-sequence
are different. That number is called Colorful Number. See Example

Example:

Given Number : 3245
Output : Colorful
Number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
this number is a colorful number, since product of every digit of a sub-sequence
are different.
That is, 3 2 4 5 (3*2)=6 (2*4)=8 (4*5)=20, (3*2*4)= 24 (2*4*5)= 40

Given Number : 326
Output : Not Colorful.
326 is not a colorful number as it generates 3 2 6 (3*2)=6 (2*6)=12.
"""


def getDigits(number):
    """
    Create a collection of all the items that we need to evaluate the product of.
    In order to do this, I am going to put each of the digits in an array.
    :param number: integer, input number
    :return: list, collection of digits in the input number
    """
    digits = list()
    while number > 0:
        x = number % 10
        number = number // 10
        digits.append(x)
    return digits[::-1]

def colorful(number):
    """
    :param number: list of integers, digits
    :return: bool
    """
    digits = getDigits(number)
    # Create a hash table
    productsList = []
    groupingOf = 1
    while groupingOf <= len(digits):
        for i in range(len(digits)):
            j = i + groupingOf
            outOfBound = False
            if j > len(digits):
                outOfBound = True
                break
            subDigits = digits[i:j]
            products = 1
            for s in subDigits:
                products *= s
            if (products in productsList) and (not outOfBound):
                return False
            else:
                productsList.append(products)
        groupingOf += 1
    return True



number = 326
print(colorful(number))