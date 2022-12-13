import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import openpyxl

#Gráfico de barras
penguins = sns.load_dataset("penguins")
#print(penguins.head())
#print(penguins.columns)
#print(penguins.info)
#print(penguins['species'].unique())

#sns.displot(penguins, x='flipper_length_mm', binwidth=3, bins=3)
#binwidth - diminui o parâmetro do eixo Y
#bins - aumenta o número de caixas


sns.displot(penguins, x="flipper_length_mm", hue="species")
#hue - junta os dados


#sns.displot(penguins, x="flipper_length_mm", hue="species", element="step")
#element é uma outra forma de apresentar
#sns.displot(penguins, x="flipper_length_mm", hue="species", multiple="stack")
#multiple é uma outra forma de apresentar
#sns.displot(penguins, x="flipper_length_mm", hue="sex", multiple="dodge")# 'dodge' não sobrepõe os dados


sns.displot(penguins, x="flipper_length_mm", col="species") #cria gráficos separador para cada valor em 'col'
plt.show()

tips = sns.load_dataset("tips")
print(tips.head())
#print(tips['day'].unique())
#sns.displot(tips, x="size", discrete=True)
# discrete - junta as caixas uma na outra
#sns.displot(tips, x="day", shrink=0.8)
#shrink - pode juntar ou separar as caixas
#plt.show()


#https://seaborn.pydata.org/tutorial/distributions.html