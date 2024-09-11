import pandas as pd

# Criar o DataFrame frutas
data_frutas = {
    'Fruta': ['Maçã', 'Banana'],
    'Quantidade': [30, 20]
}
df_frutas = pd.DataFrame(data_frutas)
print("DataFrame frutas:")
print(df_frutas)

# Criar o DataFrame vendas_frutas
vendas_frutas = {
    'Fruta': ['Maçã', 'Banana'],
    'Vendas 2022': [1000, 700],
    'Vendas 2023': [5000, 2000]
}
df_vendas_frutas = pd.DataFrame(vendas_frutas)
print("\nDataFrame vendas_frutas:")
print(df_vendas_frutas)