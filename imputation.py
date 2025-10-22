import pandas as pd
import numpy as np
data = {
        'Age': [25, 30, np.nan, 35, 40],
        'Salary': [50000, np.nan, 55000, 69000, 70000]
    }
df = pd.DataFrame(data)
print(df)

print("\nChoose Imputation Method:")
print("1. Simple Imputation ")
print("2. Imputation with Extension ")
choice = int(input( "1 or 2: "))

df_imputed = df.copy()

for col in df.columns:
    if df[col].dtype in [np.float64, np.int64]:
        missing_val = df[col].isna()
        non_missing_val = df[col].notna()     

        mean_val = np.sum(non_missing_val) / len(non_missing_val)

        for i in range(len(df[col])):          # here we replace nan values with mean
            if pd.isna(df[col][i]):
                df_imputed.loc[i, col] = mean_val

        if choice == 2:
            df_imputed[col + "_was_missing"] = missing_val

    else:          # categorical data
        non_missing = [x for x in df[col] if pd.notna(x)]
        mode_val = max(non_missing, key=non_missing.count) if non_missing else "Unknown"
        missing_val = df[col].isna()

        for i in range(len(df[col])):
            if pd.isna(df[col][i]):
                df_imputed.loc[i, col] = mode_val

        if choice == 2:
            df_imputed[col + "_was_missing"] = missing_val

print(df_imputed)