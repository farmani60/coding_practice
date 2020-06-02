"""
O(1) describes algorithms that take the same amount of time to compute
regardless of the input size.

For instance, if a function takes the identical time to process ten elements as
well as 1 million items, then we say that it has a constant growth rate or O(1).
Let’s see some cases.

Examples of constant runtime algorithms:

* Find if a number is even or odd.
* Check if an item on an array is null.
* Print the first element from a list.
* Find a value on a map.
"""

def isEvenOrOdd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

isEvenOrOdd(10)
isEvenOrOdd(1000001)

"""
Only a hash table with a perfect hash function will have a worst-case runtime of 
O(1). The ideal hash function is not practical, so there will be some collisions 
and workarounds that leads to a worst-case runtime of O(n). Still, on average, 
the lookup time is O(1).
"""
def getWordFrequency(dictionary, word):
    return dictionary[word]

dictionary = {'the': 22038615, 'be': 12545825, 'and': 10741073, 'of': 10343885,
              'a': 10144200, 'in': 6996437, 'to': 6332195}

print(getWordFrequency(dictionary, 'to'))