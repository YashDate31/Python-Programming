A = {10, 20, 30}
B = {20, 30, 40}

print("Intersection:", A & B)
print("Union:", A | B)
print("Difference:", A - B)
print("Symmetric Difference:", A ^ B)

# Clear set
A.clear()
A.add(100)
d = A.copy()
print(d)

print("After clearing A:", A)