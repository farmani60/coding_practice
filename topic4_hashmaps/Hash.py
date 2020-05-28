
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
