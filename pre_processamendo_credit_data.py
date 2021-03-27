import pandas as pd
base = pd.read_csv('credit_data.csv')
base.describe()
base.loc[base['age'] < 0]
# apagar a coluna
base.drop('age', 1, inplace=True)
# apagar somente os registros com problema
base.drop(base[base.age < 0].index, inplace=True)
# preencher os valores manualmente
