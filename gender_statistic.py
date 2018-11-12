import os
import pandas as pd
import matplotlib.pyplot as plt
import collections

def draw():
    female_statistic = {}
    male_statistic = {}

    for filename in os.listdir('babynames/'):
        data = pd.read_csv('babynames/' + filename, header=None)

        yer = filename[3:7]
        data.columns = ['name', 'gender', yer]

        mal = data[data['gender'] == 'M']
        fem = data[data['gender'] == 'F']
        male_counter = mal[yer].sum()
        female_counter = fem[yer].sum()
        male_statistic.update({yer: male_counter})
        female_statistic.update({yer: female_counter})

    male_sorted_statistic = collections.OrderedDict(sorted(male_statistic.items()))
    female_sorted_statistic = collections.OrderedDict(sorted(female_statistic.items()))

    male_keys = male_sorted_statistic.keys()
    female_keys = female_sorted_statistic.keys()

    male_vals = male_sorted_statistic.values()
    female_vals = female_sorted_statistic.values()

    fig, axs = plt.subplots(1, 2, figsize=(10,10))

    axs[0].bar(male_keys, male_vals, label="male")
    axs[0].legend()
    axs[1].bar(female_keys, female_vals, label="female")
    axs[1].legend()
    fig.suptitle('gender statistic')
    fig.show()
