import numpy as np
import pandas as pd



dataset = pd.read_csv("D:/Data-Science-Analytics/data/earthquakes.csv", usecols = ['time','title','place','magType','mag','alert','tsunami'])


#criando uma coluna
dataset['ones']=1

#print(dataset.head())

#Criando uma nova coluna de conparação
dataset['mag_negative'] = dataset.mag < 0

#print(dataset.head())

#print(dataset.place.str.extract(r', (.*$)')[0].sort_values().unique())

#problema de reconhecimento de entidade
dataset['parsed_place'] = dataset.place.str.replace(r'.*of ','').str.replace(r'the','').str.replace(r'CA$', 'California').str.replace(r'NV$','Nevada').str.replace(r'MX$','Mexico').str.replace(r'region$','').str.replace(r'northern','').str.replace(r'Fiji Islands','Fiji').str.replace(r'^.*,','').str.strip()

#analisando que sobraram
#print(dataset.parsed_place.sort_values().unique())


#Com o método assign(),
#print(dataset.assign(in_ca = dataset.parsed_place.str.endswith('California'),in_alaska = dataset.parsed_place.str.endswith('Alaska')).head())


tsunami = dataset[dataset.tsunami == 1]
no_tsunami = dataset[dataset.tsunami == 0]


#print(tsunami.shape, no_tsunami.shape)


#print(pd.concat([tsunami, no_tsunami]).shape)

#print(tsunami.append(no_tsunami).shape)


additional_columns = pd.read_csv("D:/Data-Science-Analytics/data/earthquakes.csv", usecols = ['tz','felt','ids'])

#print(pd.concat([dataset.head(2), additional_columns.head(2)] ,axis = 1))



additional_columns = pd.read_csv("D:/Data-Science-Analytics/data/earthquakes.csv", usecols =['tz','felt','ids','time'],index_col = 'time')

#print(pd.concat([dataset.head(2), additional_columns.head(2)], axis =1))



#print(pd.concat([tsunami.head(2), no_tsunami.head(2).assign( type = 'earthquake')],join = 'inner'))


#print(pd.concat([tsunami.head(2), no_tsunami.head(2).assign(type='earthquake')],join = 'inner', ignore_index = True))

#deletando coluna
#del dataset['ones']

#print(dataset.columns)

try:
    del dataset['ones']
except KeyError:
    # lide com o erro aqui.
    pass


mag_negative = dataset.pop('mag_negative')

#print(dataset.columns)


#print(mag_negative.value_counts())

#print(dataset[mag_negative].head())

#print(dataset.drop([0,1]).head(2))

#print(dataset.drop(columns =[col for col in dataset if col not in ['alert','mag','title','tsunami']]).head())

#print(dataset.drop( columns=[col for col in dataset if col not in ['alert','mag','title','mag','tsunami']]).equals (dataset.drop( columns=[col for col in dataset if col not in ['alert','mag','title','mag','tsunami']], axis = 1)))

dataset.drop(columns=[col for col in dataset.columns if col not in ['alert','mag','title','time']], inplace = True)

print(dataset.head())

