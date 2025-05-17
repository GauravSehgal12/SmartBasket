import pandas as pd

rules = pd.read_pickle('rules.pkl')
print(rules.head())
print(rules.shape)