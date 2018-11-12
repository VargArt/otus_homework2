import os
import pandas as pd
import matplotlib.pyplot as plt
import collections

def draw():
    fixed_years_statistic = ['1881', '1894', '1994', '2010']

    statistic = {}
    reverse_statistic = {}

    for filename in os.listdir('babynames/'):
        data = pd.read_csv('babynames/' + filename, header=None)

        yer = filename[3:7]
        data.columns = ['name', 'gender', yer]

        print(yer)

        fixed_statistic = {}
        reverse_fixed_statistic = {}

        for key in fixed_years_statistic:
            if yer == key:
                for index, row in data.iterrows():

                    k = row['name'][0]
                    if k in fixed_statistic:
                        fixed_statistic.update({k: (row[yer] + fixed_statistic[k])})
                    else:
                        fixed_statistic.update({k: row[yer]})

                    k_rev = row['name'][-1]
                    if k in reverse_fixed_statistic:
                        reverse_fixed_statistic.update({k_rev: (row[yer] + reverse_fixed_statistic[k])})
                    else:
                        reverse_fixed_statistic.update({k_rev: row[yer]})

                fs = collections.OrderedDict(sorted(fixed_statistic.items()))
                statistic.update({yer: fs})

                fs_rev = collections.OrderedDict(sorted(reverse_fixed_statistic.items()))
                reverse_statistic.update({yer: fs_rev})

                break


    fig, ax = plt.subplots()
    for (key, val) in statistic.items():
        ax.plot(val.keys(), val.values(), label=key + " first letter")

    for (key, val) in reverse_statistic.items():
        ax.plot(val.keys(), val.values(), label=key + " last letter")

    ax.legend()
    plt.show()

