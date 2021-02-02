import numpy as np
import pandas as pd



dataset = pd.read_csv("D:/Data-Science-Analytics/data/earthquakes.csv")



#obtendo estatísticas resumidas
#print(dataset.describe())

#print(dataset.describe(include = np.object))


#Até agora, sabemos que a coluna de alerta é uma string de dois valores únicos e o valor mais comum é 'verde' com muitos valores nulos.
#print(dataset.alert.unique())


#podemos verificar isso com uma tabela de frequência usando value_counts():
print(dataset.alert.value_counts())
