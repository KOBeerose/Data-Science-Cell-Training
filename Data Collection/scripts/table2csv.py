import pandas as pd

df = pd.read_html('https://data-science-cell.netlify.app/', )
df = df[0]
df.drop(df.columns[-1], axis=1, inplace=True)
# df.drop(df[df['column'] == 'value'], axis=1, inplace=True)
# df['Timestamp'] = df['Timestamp'].map(lambda x: x[:-3])

print(df)
df.to_csv('data-cell-memebers.csv', index=False)


