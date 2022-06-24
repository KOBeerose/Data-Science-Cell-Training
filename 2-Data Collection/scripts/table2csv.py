import pandas as pd

df = pd.read_html('https://www.investing.com/crypto/bitcoin/historical-data', )
df = df[0]

# droping some unncessary data
"""df.drop(df.columns[-1], axis=1, inplace=True)

df.drop(df[df['column'] == 'value'], axis=1, inplace=True)

df['Timestamp'] = df['Timestamp'].map(lambda x: x[:-3])

print(df)

# saving Dataframe to a csv file
df.to_csv('data-cell-memebers.csv', index=False)"""


print(df)