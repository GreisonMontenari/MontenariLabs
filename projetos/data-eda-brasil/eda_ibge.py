import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar dados
# Aqui usamos um exemplo fictício de dataset com nome populacao_municipios.csv
# Certifique-se de ter o arquivo correto em /dados/
df = pd.read_csv("dados/populacao_municipios.csv")

# Exibir primeiras linhas
print(df.head())

# Gráfico de distribuição
plt.figure(figsize=(10,6))
sns.histplot(df["populacao"], bins=30, kde=True)
plt.title("Distribuição da População dos Municípios")
plt.xlabel("População")
plt.ylabel("Número de Municípios")
plt.tight_layout()
plt.savefig("distribuicao_populacao.png")
plt.show()
