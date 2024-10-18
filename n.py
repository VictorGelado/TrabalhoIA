import pandas as pd

# Carregar o dataset
df = pd.read_csv('soil_data.csv')

# Exibir todas as colunas
print("Todas as colunas no dataset:")
print(df.columns)

# Número total de variáveis
num_colunas = len(df.columns)
print("\nNúmero total de variáveis:", num_colunas)
