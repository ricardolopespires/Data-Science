import datetime
import numpy as np
import pandas as pd


# definindo uma semente para reprodutibilidade
np.random.seed(0)
data = pd.Series(np.random.rand(5), name = 'random')


#print(data)

# definindo semente para que o resultado seja reproduzível
np.random.seed(0)

dataset = pd.DataFrame({'random':np.random.rand(5),
              'text':['hot','warn', 'cool','cold', None],
              'truth':[np.random.choice([True, False]) for _ in range(5)]
              },
             index = pd.date_range( end = datetime.date(2019,4,21), freq = '1D', periods = 5, name = 'date')
             )



#print(dataset)     

dataset = pd.DataFrame([{'mag':5.2, 'place':'California'},
                        {'mag': 1.2, 'place':'Alaska'},
                        {'mag':0.2, 'place':'California'},])

#print(dataset)

list_of_tuples = [(n, n**2, n**3) for n in range(5)]
#print(list_of_tuples)

dataset = pd.DataFrame(list_of_tuples, columns =['n', 'n_squared', 'n_cubed'])

#print(dataset)
from array import array

dataset = pd.DataFrame(np.array([[0,0,0],[1,1,1],[2,4,8],[3,9,27],[4,16,64]]),columns = ['n', 'n_squared','n_cubed'])


#print(dataset)

#print(!wc -1 D:/Programação/hands-data-analysis-pandas-visualization/9781789615326_Code/9781789615326_Code/Hands-On-Data-Analysis-with-Pandas-master/ch_02/data/earthquakes.csv)

#print(!ls -lh data | grep D:/Programação/hands-data-analysis-pandas-visualization/9781789615326_Code/9781789615326_Code/Hands-On-Data-Analysis-with-Pandas-master/ch_02/data/earthquakes.csv)                    

dataset = pd.read_csv('D:/Programação/hands-data-analysis-pandas-visualization/9781789615326_Code/9781789615326_Code/Hands-On-Data-Analysis-with-Pandas-master/ch_02/data/earthquakes.csv')
#print(dataset.head())


import sqlite3

with sqlite3.connect('D:/Data-Science- Analytics/data/quakes.db') as connection:
    pd.read_csv('D:/Data-Science- Analytics/data/tsunamis.csv').to_sql('tsunamis',connection, index = False, if_exists = 'replace')






#consultando o banco de dados
with sqlite3.connect('D:/Data-Science- Analytics/data/quakes.db')as connection:
    tsunamis = pd.read_sql('SELECT * FROM tsunamis', connection)

print(tsunamis.head())
