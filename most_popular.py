import os
import pandas as pd
import matplotlib.pyplot as plt

def draw():
    popular_year_names = {}
    counter = 0

    for filename in os.listdir('babynames/'):
        data = pd.read_csv('babynames/' + filename, header=None)

        yer = filename[3:7]
        data.columns = ['name', 'gender', yer]

        most_popular = data[data[yer] == data[yer].max()]
        counter+=1
        name = most_popular['name'].values[0]
        if name in popular_year_names:
            popular_year_names.update({name: (popular_year_names[name]+1)})
        else:
            popular_year_names.update({name: 1})

    plt.pie(list(popular_year_names.values()), labels=tuple(popular_year_names.keys()))
    plt.show()
