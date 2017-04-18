import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def agg_count(row):
    count_x = getattr(row, 'Count_x', 0)
    count_y = getattr(row, 'Count_y', 0)
    count = getattr(row, 'Count', 0)

    row.Count = count + count_x + count_y
    return row


def top3(list_year, PATH):
    cols = ['Name', 'Gender', 'Count']
    names_all = None
    for year in list_year:
        names_year = pd.read_csv(PATH + 'yob{}.txt'.format(year), names=cols)
        if names_all is None:
            names_all = names_year
        else:
            names_all = pd.merge(names_all, names_year, on=['Name', 'Gender']).apply(agg_count, axis=1)
    names_all['total'] = names_all.sum(axis=1)
    #print(names_all)

    result = names_all.sort_values(by='total', ascending=False).head(3)
    return result['Name'].values


def dynamics(list_year, PATH):
    cols = ['Name', 'Gender', 'Count']
    names_all = None
    list_f = []
    list_m = []
    for year in list_year:
        names_year = pd.read_csv(PATH + 'yob{}.txt'.format(year), names=cols)
        f = names_year[names_year.Gender == 'F'].Count.sum()
        m = names_year[names_year.Gender == 'M'].Count.sum()
        list_f.append(f)
        list_m.append(m)
    result = {'F': list_f, 'M': list_m}
    return result


def main():
    PATH = r'C:\Users\swetlanka\Documents\GitHub\py3\4-1\names\\'
    list_year = [1900,1950,2000]
    print('count_top3({}) =='.format(list_year), top3(list_year, PATH))
    print('count_dynamics({}) =='.format(list_year), dynamics(list_year, PATH))

main()