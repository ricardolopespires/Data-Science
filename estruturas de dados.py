import numpy as np


dataset = np.genfromtxt('D:\Programação\hands-data-analysis-pandas-visualization\9781789615326_Code\9781789615326_Code\Hands-On-Data-Analysis-with-Pandas-master\ch_02\data\example_data.csv',
                        delimiter = ';', names = True, dtype = None, encoding = "UTF")

#print(dataset)


#print(dataset.shape)

#print(dataset.dtype)

#print(%%timeit)

array_dict = {}

for i, col in enumerate(dataset.dtype.names):
    array_dict[col] = np.array([row[i] for row in dataset])

#print(array_dict)


#print(array_dict['mag'].max())

data = np.array([value[array_dict['mag'].argmax()] for key, value in array_dict.items()])

#print(data)

import pandas as pd

place = pd.Series(array_dict['place'], name = 'place')
#print(place)


place_index = place.index

#print(place_index)

#print(place_index.values)


data = np.array([1,1,1]) + np.array([-1, 0, 1])

#print(data)

data = pd.Series(np.linspace(0,10, num=5)) + pd.Series(np.linspace(0,10, num = 5), index = pd.Index([1,2,3,4,5]))

#print(data)

dataset = pd.DataFrame(array_dict)

#print(dataset)

#print(dataset.dtypes)

print(dataset + dataset)
