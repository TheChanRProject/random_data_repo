import numpy as np
import pandas as pd

X = np.random.randint(0, 1000, (2000, 20))

df = pd.DataFrame(X, columns=[f'col_{i}' for i in range(1, 21)])

df.to_csv("random_data.csv", index=False)


read_df = pd.read_csv("random_data.csv")

read_df.shape

read_df.head()

type(read_df['col_1'])

read_df['col_1'][:50]



len([1,2,3,4,5])
sum([1,2,3,4,5])

def prod(x):
    return np.prod(x)

prod((1,2,3,4,5))
