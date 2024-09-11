import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame()


df['Column A'] = ['Value 1', 'Value 2']
df['Column B'] = [10, 20]
df['Column С'] = [5, 6]
df['Column D'] = [33, 36]

print(df)

df['Column B'] = df['Column B'].astype(float)
print(df)

df.plot.hist(bins=20)
plt.show()





