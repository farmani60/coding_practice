
def isPrime(number):
    if all([number % i != 0 for i in range(2, number)]):
        return True
    else:
        return False

def getDigits(number):
    digits = []
    while number != 0:
        digits.append(number % 10)
        number = number // 10
    return digits[::-1]

def colourful(number):
    digits = getDigits(number)
    groupingOf = 1
    productsList = []
    while groupingOf < len(digits):
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

print(colourful(3426))