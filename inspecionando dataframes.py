import numpy as np
import pandas as pd



dataset = pd.read_csv("D:/Data-Science-Analytics/data/earthquakes.csv")

#print(dataset.empty)


#queremos saber o número de observações (linhas) e o número de variáveis (colunas) que temos. 
#print(dataset.shape)

#Mostrando os dados, podemos usar os métodos head()
#print(dataset.head())


#para obter as duas últimas linhas
#print(dataset.tail(2))


#Vamos usar o atributo de colunas
#print(dataset.columns)

#podemos ver facilmente quando as colunas estão sendo armazenadas com o tipo de dados
#print(dataset.dtypes)

#podemos usar o método info () para ver quantas entradas não nulas de cada coluna temos e obter informações sobre nosso Índice.
#print(dataset.info())
