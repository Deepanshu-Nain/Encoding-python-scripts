import pandas as pd

# now lets make a dataframe on which we apply ordinal encoding

df = pd.DataFrame({ "size" : ['small','medium','large','small']})

print(df)   

#now lets do the ordinal encoding

order =['small','medium','large']
encoded_values =[]

for sizes in df['size']:
    encoded_values.append(order.index(sizes))

df['new_column'] = encoded_values
print(df)




