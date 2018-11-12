import os
import pandas as pd
import matplotlib.pyplot as plt
import collections

def draw():
    names = ['Tom', 'Bruce', 'George', 'Paul', 'John', 'Terence']

    statistic = {}

    for name in names:
        statistic.update({name: {}})

    for filename in os.listdir('babynames/'):
        data = pd.read_csv('babynames/' + filename, header=None)

        yer = filename[3:7]
        data.columns = ['name', 'gender', yer]

        for name in names:
            statistic[name][yer] = 0
            dt = data[data["name"] == name]
            if not dt.empty:
                statistic[name][yer] = dt[yer].values[0]

    fig, ax = plt.subplots()
    for (key, val) in statistic.items():
        ordered_statistic = collections.OrderedDict(sorted(val.items()))
        ax.plot(ordered_statistic.keys(), ordered_statistic.values(), label=key)

    ax.legend()
    plt.show()
