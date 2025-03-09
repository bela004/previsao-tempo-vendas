import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1) Manipulação do DataFrame com Pandas
dados = {
    "Data": ["15/01/2025"] * 5,
    "Cidade": ["São Paulo", "Rio de Janeiro", "Curitiba", "Porto Alegre", "Salvador"],
    "Temperatura Máxima (°C)": [30.5, 35.0, 24.0, 28.0, 31.0],
    "Temperatura Mínima (°C)": [22.0, 25.0, 18.0, 20.0, 24.5],
    "Precipitação (mm)": [12.0, np.nan, 8.0, 15.0, np.nan],
    "Umidade Relativa (%)": [78, 70, np.nan, 82, 80]
}

df = pd.DataFrame(dados)

# Substituindo valores ausentes
media_precipitacao = df["Precipitação (mm)"].mean()
df["Precipitação (mm)"].fillna(media_precipitacao, inplace=True)

mediana_umidade = df["Umidade Relativa (%)"].median()
df["Umidade Relativa (%)"].fillna(mediana_umidade, inplace=True)

# Adicionando coluna Amplitude Térmica
df["Amplitude Térmica"] = df["Temperatura Máxima (°C)"] - df["Temperatura Mínima (°C)"]

# Filtrando cidades com Temperatura Máxima acima de 30°C
df_filtrado = df[df["Temperatura Máxima (°C)"] > 30]

# Reordenando colunas
colunas_ordenadas = ["Data", "Cidade", "Temperatura Máxima (°C)", "Temperatura Mínima (°C)", "Amplitude Térmica", "Precipitação (mm)", "Umidade Relativa (%)"]
df = df[colunas_ordenadas]
df_filtrado = df_filtrado[colunas_ordenadas]

# Exibir os DataFrames processados
print("DataFrame Completo:")
print(df)
print("\nDataFrame Filtrado:")
print(df_filtrado)

# 2) Gráfico de linha da evolução da temperatura
tempo = list(range(25))  # Horas do dia
temperaturas = [15 + (x * 1.25) if x <= 12 else 30 - ((x - 12) * 1) for x in tempo]

plt.figure(figsize=(10, 5))
plt.plot(tempo, temperaturas, marker='o', linestyle='-', color='b')
plt.title("Evolução da Temperatura ao Longo do Dia")
plt.xlabel("Hora do Dia")
plt.ylabel("Temperatura (°C)")
plt.grid(True)
plt.show()

# 3) Análise de vendas com Seaborn
dados_vendas = {
    "Dia": ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"],
    "Vendas": [500, 600, 700, 650, 800, 900, 750],
    "Clientes": [50, 60, 65, 55, 70, 80, 75],
    "Lucro": [100, 120, 150, 130, 180, 200, 170]
}

df_vendas = pd.DataFrame(dados_vendas)

# Gráfico de barras - Vendas por dia
plt.figure(figsize=(8, 5))
sns.barplot(x="Dia", y="Vendas", data=df_vendas, palette="viridis")
plt.title("Total de Vendas por Dia")
plt.xlabel("Dia da Semana")
plt.ylabel("Total de Vendas")
plt.show()

# Gráfico de dispersão - Clientes vs. Vendas
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Clientes", y="Vendas", data=df_vendas, color='r')
plt.title("Relação entre Número de Clientes e Vendas")
plt.xlabel("Número de Clientes")
plt.ylabel("Total de Vendas")
plt.show()

# Heatmap - Correlação entre variáveis
plt.figure(figsize=(8, 5))
sns.heatmap(df_vendas.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlação entre Vendas, Clientes e Lucro")
plt.show()
