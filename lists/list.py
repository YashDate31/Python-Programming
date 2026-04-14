# 1. Create List
arr = [130, 320, 310, 43]
print("Original List:", arr)

# 2. Access List
print("First element:", arr[0])
print("Last element:", arr[-1])

# 3. Update List

# ➤ Add item
arr.append(50)
print("After adding element:", arr)

# ➤ Remove item
arr.remove(130)
print("After removing element:", arr)


#printing max

print("Max number",max(arr))
#sorting list
arr.sort()
print("sorting list",arr)
# 4. Delete List
del arr
print("List deleted")