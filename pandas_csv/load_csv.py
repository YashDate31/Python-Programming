import pandas as pd

# Load a CSV file into a Pandas DataFrame
try:
    df = pd.read_csv("CardioGoodFitness.csv")

    # Display the first 5 rows of the DataFrame
    print("First 5 rows of the DataFrame:")
    print(df.head())

    # Display basic information about the DataFrame
    print("\nDataFrame Info:")
    df.info()

    # Display descriptive statistics
    print("\nDescriptive Statistics:")
    print(df.describe())

except FileNotFoundError:
    print("Error: CardioGoodFitness.csv not found. Please make sure the file is in the same directory.")

