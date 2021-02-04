import numpy as np
import pandas as pd



dataset = pd.read_csv("D:/Data-Science-Analytics/data/earthquakes.csv")



#obtendo estatísticas resumidas
#print(dataset.describe())

#print(dataset.describe(include = np.object))


#Até agora, sabemos que a coluna de alerta é uma string de dois valores únicos e o valor mais comum é 'verde' com muitos valores nulos.
#print(dataset.alert.unique())


#podemos verificar isso com uma tabela de frequência usando value_counts():
#print(dataset.alert.value_counts())

#vamos pegar a coluna mag, que contém as magnitudes dos terremotos
#print(dataset.mag)


#vamos pegar a coluna mag, que contém as magnitudes dos terremotos em formato de  dicionário
#print(dataset['mag'])


#Passando uma lista para a pesquisa em formato de dicionário.
#print(dataset[['mag','title']])



#Selecionando várias colunas
dados = dataset[['title','time'] + [col for col in dataset.columns if col.startswith('mag')]]

dados = [col for col in dataset if col.startswith('mag')]

#adicionamos este resultado às outras duas colunas que queríamos manter (título e tempo)

dados = ['title','time']+[col for col in dataset.columns if col.startswith('mag')]

#usando esta lista para executar a seleção de coluna real no dataframe (o resultado é omitido por questões de brevidade)
dados = dataset[['title','time'] + [col for col in dataset.columns if col.startswith('mag')]]

#print(dados)

#O fatiamento do DataFrame
#print(dataset[100:103])
                
#Encadeamento
#print(dataset[['title','time']][100:103])

#print(dataset[100:103][['title','time']].equals(dataset[['title','time']][100:103]))


#print(dataset['title'])


dataset.loc[100:103, 'title'] = dataset.loc[100:103, 'title'].str.lower()

#print(dataset.loc[100:103, 'title'])


#Selecionar várias linhas e colunas ao mesmo tempo
#Index inclusivo
#print(dataset.loc[10:15,['title','mag']])



#Selecionar várias linhas e colunas ao mesmo tempo
#Index exclusivo
#print(dataset.iloc[10:15,[19,8]])


#sistema de faiamento não só para linhas  mais também serve para as colunas
#print(dataset.iloc[10:15, 8:10].equals(dataset.loc[10:14, 'mag':'magType']))


#print(dataset.at[10, 'mag'])

#print(dataset.iat[10,8])


#print(dataset.mag > 2)

#obter o subconjunto do dataframe onde a magnitude do terremoto foi maior ou igual a 7,0
#print(dataset[dataset.mag >= 7.0])


#print(dataset.loc[dataset.mag >= 7.0, ['alert','mag','magType', 'title','tsunami','type']])

#Operador AND
print(dataset.loc[(dataset.tsunami == 1) & (dataset.alert == 'red'), ['alert', 'mag', 'magType','tsunami','type']])
