# Create Set
s = {10, 20, 30, 40}
print("Original Set:", s)

# Access Set (using loop)
print("Access elements:")
for i in s:
    print(i)

# Update Set (Add & Remove)
s.add(50)          # add element
s.remove(20)       # remove element
print("Updated Set:", s)

# Delete Set
del s
# print(s)  # this will give error because set is deleted