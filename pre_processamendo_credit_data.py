import pandas as pd
base = pd.read_csv('credit_data.csv')
base.describe()
base.loc[base['age'] < 0]
# apagar a coluna
base.drop('age', 1, inplace=True)
# apagar somente os registros com problema
base.drop(base[base.age < 0].index, inplace=True)
# preencher os valores manualmente
# ou
# preencher os valores com a media de idade
base.mean()
base['age'].mean()
base['age'][base.age > 0].mean()
base.loc[base.age < 0, 'age'] = 40.92

# verificar valores nulos
pd.isnull(base['age'])
base.loc[pd.isnull(base['age'])]

previsores = base.iloc[:, 1:4].values #cria uma variavel com valores das colunas
# :(dois pontos) significa todas as linhas
# 1:4 vai pegar dados da coluna 1 até 3
classe = base.iloc[:, 4].values
import numpy as np
from sklearn.impute import SimpleImputer 
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(previsores[:, 0:3])
previsores[:, 0:3] = imputer.transform(previsores[:, 0:3])

