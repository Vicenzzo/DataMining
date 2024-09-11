import pandas as pd

df = pd.read_csv('archive/tmdb_5000_movies.csv')

print("DataFrame importado do CSV:")
print(df.head())

print("\nTipos de dados de cada coluna:")
print(df.dtypes)

valores_coluna = df['title']
print("\nValores da coluna 'title':")
print(valores_coluna.head()) 

valor_maximo = df['budget'].max()
print("\nValor máximo da coluna 'budget':")
print(valor_maximo)


dados_filtrados = df[df['title'] == 'Inception']
print("\nDados onde 'title' é igual a 'Inception':")
print(dados_filtrados)
