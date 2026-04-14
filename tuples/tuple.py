# 1. Create Tuple
t = (10, 20, 30, 40)
print("Original Tuple:", t)

# 2. Access Tuple
print("First element:", t[0])
print("Last element:", t[-1])

# 3. Print Tuple
print("Printing Tuple:", t)

# 4. Convert Tuple → List
lst = list(t)
print("Converted to List:", lst)

# 5. Update using List (since tuple is immutable)
lst.append(50)
print("After adding element in list:", lst)

# 6. Convert List → Tuple
t = tuple(lst)
print("Converted back to Tuple:", t)

# 7. Delete Tuple
del t
print("Tuple deleted")