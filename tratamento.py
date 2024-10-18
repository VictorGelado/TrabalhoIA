import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('soil_data.csv')

print(df.dtypes)

numeric_cols = df.select_dtypes(include=['float64', 'int64'])

corr_matrix = numeric_cols.corr()

plt.figure(figsize=(10,8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Matriz de Correlação")
plt.show()

correlated_features = corr_matrix[abs(corr_matrix) > 0.8]
print("Variáveis altamente correlacionadas:\n", correlated_features)

missing_data = df.isnull().sum()
print("Valores ausentes por coluna:\n", missing_data)

df[numeric_cols.columns] = df[numeric_cols.columns].fillna(df.mean())

categorical_cols = df.select_dtypes(include=['object'])
df[categorical_cols.columns] = df[categorical_cols.columns].fillna(df.mode().iloc[0])


print("Dados faltantes após o tratamento:\n", df.isnull().sum())
