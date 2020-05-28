import collections

# Creating Chain Map
dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day4': 'Thu'}

res = collections.ChainMap(dict1, dict2)

# Creating a single dictionary
print(res.maps, '\n')

print('Keys = {}'.format(list(res.keys())))
print('Values = {}'.format(list(res.values())))
print()

# Print all the elements from the result
print('elements:')
for key, val in res.items():
    print('{} = {}'.format(key, val))
print()

# Map reordering
res1 = collections.ChainMap(dict1, dict2)
res2 = collections.ChainMap(dict2, dict1)

print(res1.maps)
print("\n")
print(res2.maps)
print("\n")

# Updating Map
print(res.maps)
print("\n")
dict2["day4"] = "Fri"
print(res.maps)
print("\n")

