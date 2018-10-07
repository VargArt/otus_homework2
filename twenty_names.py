import os
import pandas as pd
import matplotlib.pyplot as plt
import collections
import seaborn as sns

years = set()
for filename in os.listdir('babynames/'):
    years.add(filename[3:7])

sorted_years = sorted(years)

yr = []
for year in sorted_years:
    yr.append(year)

year_step = (int(yr[len(yr) - 1]) - int(yr[0]))/10

cur_year = int(yr[0])
st_year = []
counter = 0

years_statistic = {}
years_frame = []
d = ['name', 'gender']

while counter < 10:
    cur_year += year_step
    st_year.append(int(cur_year))
    counter += 1
    years_frame.append(pd.DataFrame(columns=d))

df = pd.DataFrame(columns=d)
print(df.head())

for filename in os.listdir('babynames/'):
    data = pd.read_csv('babynames/' + filename, header=None)

    yer = filename[3:7]
    data.columns = ['name', 'gender', yer]

    merged = pd.merge(df, data, how='outer', on=['name', 'gender'])
    df = merged
    print(df.size)

    i = 0
    while i < 10:
        if int(filename[3:7]) <= st_year[i]:
            years_frame[i] = pd.merge(years_frame[i], data, how='outer', on=['name', 'gender'])
            print(years_frame[i].head())
            break
        i += 1

male_names = set()
female_names = set()
for frame in years_frame:
    frame.fillna(0)
    frame['max'] = frame.sum(axis=1)
    female_frame = frame[frame['gender'] == 'F']
    male_frame = frame[frame['gender'] == 'M']

    fem = female_frame[female_frame['max'] == female_frame['max'].max()]
    female_names.add(fem['name'].values[0])
    mal = male_frame[male_frame['max'] == male_frame['max'].max()]
    male_names.add(mal['name'].values[0])

df = df.fillna(0)

female_names_counters = {}
for name in female_names:
    years_counter = []
    a = df[df['name'] == name]
    for year in sorted_years:
        b = a[year].values[0]
        years_counter.append(b)
    female_names_counters[name] = years_counter

male_names_counters = {}
for name in male_names:
    years_counter = []
    a = df[df['name'] == name]
    for year in sorted_years:
        b = a[year].values[0]
        years_counter.append(b)
    male_names_counters[name] = years_counter

fig, ax = plt.subplots()
for (key, val) in male_names_counters.items():
    ax.plot(sorted_years, val, label=key)

for (key, val) in female_names_counters.items():
    ax.plot(sorted_years, val, label=key)

ax.legend()
plt.show()
a = 0