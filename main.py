import pandas as pd

print("--- House Price Project Started ---")

# Creating a tiny dataset manually so you don't need a CSV yet
data = {
    'SqFt': [1000, 1500, 2000, 2500],
    'Price': [200000, 300000, 400000, 500000]
}

df = pd.DataFrame(data)
print("Here is my starting data:")
print(df)

print("\nNext step: Downloading the full Kaggle dataset!")