
# Accessing values in dictionary

# Declare a dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# Accessing the dictionary with its key
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

# Updating existing entry
dict['Age'] = 8
# Add new entry
dict['School'] = 'DPS School'

print("dict['School']: ", dict['School'])
print("dict['Age']: ", dict['Age'])

# Remove entry with key Name
del dict['Name']
print(dict)

# Remove all the entries in dictionary
dict.clear()
print(dict)

# Delete entire dictionary
del dict

# To study: https://dbader.org/blog/python-dictionaries-maps-and-hashtables
squares = {x: x**2 for x in range(10)}
print(squares)
print(squares[0].__hash__)

import collections

d = collections.OrderedDict(one=1, two=2, three=3)
print('\n')
d['four'] = 4
print('\n')
print(d)
print('\n')
print(d.keys())

from collections import defaultdict
dd = defaultdict(list)
dd['dogs'].append('Rufus')
dd['dogs'].append('Kathrin')
dd['dogs'].append('Mr Sniffles')

print(dd)

