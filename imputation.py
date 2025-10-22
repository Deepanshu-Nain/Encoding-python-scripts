import pandas as pd
import numpy as np
data = {
        'Age': [25, 30, np.nan, 35, 40],
        'Salary': [50000, np.nan, 55000, 69000, 70000]
    }
df = pd.DataFrame(data)
print(df)

print("Imputation Methods:")
print("1. Simple Imputation ")
print("2. Imputation with Extension ")

choice = int(input("pick any imputation method you want to use : "))

if choice == 1:   # simple imputation

    mean_val_col1 = df['Age'].mean()
    mean_val_col2 = df['Salary'].mean()

    df['Age'] = df['Age'].fillna(mean_val_col1)
    df['Salary'] = df['Salary'].fillna(mean_val_col2)

    print(df)

elif choice == 2:   # imputation with extension

    df['Age_was_missing'] = df['Age'].isna()
    df['Salary_was_missing'] = df['Salary'].isna()

    mean_val_col1 = df['Age'].mean()
    mean_val_col2 = df['Salary'].mean()

    df['Age'] = df['Age'].fillna(mean_val_col1)
    df['Salary'] = df['Salary'].fillna(mean_val_col2)

    print(df)

else :
    print("Invalid Input")
