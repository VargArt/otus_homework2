import os
import pandas as pd
import matplotlib.pyplot as plt
import collections
import seaborn as sns

counters = {}

for filename in os.listdir('babynames/'):
    data = pd.read_csv('babynames/' + filename, header=None)

    yer = filename[3:7]
    data.columns = ['name', 'gender', yer]

    sorted_frame = data.sort_values(by=[yer], ascending=False)

    num = int(sorted_frame[yer].sum()/2)
    num_act = 0
    cnt = 0

    for index, row in sorted_frame.iterrows():
        cnt += 1
        num_act += int(row[yer])
        if num < num_act:
            counters.update({yer: cnt})
            break


od = collections.OrderedDict(sorted(counters.items()))

fig, ax = plt.subplots()

ax.plot(od.keys(), od.values(), label="year")
plt.show()

a = 0