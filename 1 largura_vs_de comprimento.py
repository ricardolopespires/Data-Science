import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


wide_dataset = pd.read_csv('D:/Programação/hands-data-analysis-pandas-visualization/9781789615326_Code/9781789615326_Code/Hands-On-Data-Analysis-with-Pandas-master/ch_03/data/wide_data.csv', parse_dates = ['date'])
long_dataset = pd.read_csv('D:/Programação/hands-data-analysis-pandas-visualization/9781789615326_Code/9781789615326_Code/Hands-On-Data-Analysis-with-Pandas-master/ch_03/data/long_data.csv', usecols =['date', 'datatype', 'value'],parse_dates=['date'])



#print(wide_dataset.head(6))


wide_dataset.plot(kind = 'line', y = ['TMAX','TMIN', 'TOBS'], x = 'date', title = 'Temperatura em NYC em outubro de 2018',figsize = (15,5)).set_ylabel('Temperature in Celsius')
#plt.show()


#print(long_dataset.head(6))


#print(long_dataset.describe(include = 'all'))


sns.set(rc={'figure.figsize':(15,5)}, style='white')
ax = sns.lineplot(data=long_dataset, hue='datatype', y='value', x='date')
ax.set_ylabel('Temperatura em Celsius')
ax.set_title('Temperatura em NYC em outubro de 2018')
#plt.show()

sns.set(rc={'figure.figsize':(20,10)},style='white',font_scale=2)
g = sns.FacetGrid(long_dataset, col='datatype',height=10)
g = g.map(plt.plot, 'date', 'value')
g.set_titles(size=25)
g.set_xticklabels(size=25)
plt.show()









