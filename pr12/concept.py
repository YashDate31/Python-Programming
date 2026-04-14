# Create Dictionary
d = {'a': 10, 'b': 20, 'c': 30}
print("Original Dictionary:", d)

# Access
print("Access value of key 'a':", d['a'])

# Update
d['b'] = 50        # update value
d['d'] = 40        # add new key
print("Updated Dictionary:", d)

# Delete
del d['c']
print("After Deletion:", d)
print("yaaaash")
# Looping
print("Looping through dictionary:")
for key, value in d.items():
    print(key, value)

# Create Dictionary from List
keys = ['x', 'y', 'z']
values = [1, 2, 3]
new_dict = dict(zip(keys, values))
print("Dictionary from list:", new_dict)