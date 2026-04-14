import pandas as pd
import numpy as np

# 1. Create Series from Array
arr = np.array([10, 20, 30, 40])
s1 = pd.Series(arr)
print("Series from Array:")
print(s1)

# 2. Create Series from List
lst = [1, 2, 3, 4]
s2 = pd.Series(lst)
print("\nSeries from List:")
print(s2)

# 3. Access element of Series
print("\nAccess element at index 2:", s2[2])

# 4. Create DataFrame using Dictionary
data = {
    'Name': ['Yash', 'Vijay', 'Rahul'],
    'Marks': [85, 90, 78]
}

df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)