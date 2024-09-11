import pandas as pd
import json

# 1. Leitura do Arquivo e Visualização das Primeiras Linhas

# Carregar o dataset

df = pd.read_csv('tmdb_5000_movies.csv')

# Mostrar as primeiras 5 linhas do dataset
print(df.head())



# 2. Demonstrar os Dados das Colunas ['title', 'cast']


# Selecionar as colunas 'title' e 'cast'
df_selected = df[['title', 'cast']]

# Mostrar as primeiras 5 linhas dessas colunas
print(df_selected.head())


# 3. Desafio: Disposição de Nomes de Atores Baseado em Seus Respectivos Filmes

# Função para extrair os nomes dos atores
def extract_actors(row):
    cast_data = json.loads(row['cast'])  # Converte string JSON para um objeto Python
    actors = [actor['name'] for actor in cast_data[:3]]  # Pega os 3 primeiros atores
    return f"{row['title']} | {', '.join(actors)}"

# Aplicar a função em cada linha do DataFrame
df_selected['actors'] = df_selected.apply(extract_actors, axis=1)

# Mostrar as primeiras 5 linhas do resultado
print(df_selected[['actors']].head())
