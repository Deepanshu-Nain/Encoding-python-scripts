import pandas as pd
import numpy as np

# creating a dataframe on which will do one hot encoding :)
df = pd.DataFrame({'Color': ['red', 'blue', 'green', 'red']})
print(df)

# first lets take out unique colors that we will going to assign one hot encoded values 
unique_colors = []
for color in df['Color']:
    if color not in unique_colors:
        unique_colors.append(color)

# now doing the one hot encoding

for color in unique_colors:
    df[color] = [1 if col == color else 0 for col in df['Color']]

print(df)
