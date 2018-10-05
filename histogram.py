import utils
import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np

BINS = 50
HOUSES_COL = 'Hogwarts House'
HOUSES = ['Ravenclaw', 'Slytherin', 'Gryffindor', 'Hufflepuff']

def plot_hist(court, df):
    ar = df[[HOUSES_COL, court]]
    ar_sort = ar.sort_values(court)
    for house_name in HOUSES:
        house = ar_sort.loc[ar_sort[HOUSES_COL] == house_name]
        house = house[court].tolist()
        _ = plt.hist(house, bins=BINS, alpha=0.5, label=house_name)
    
    plt.ylabel('count')
    plt.xlabel('notes')
    plt.title(court)
    plt.legend(loc='upper right')
    plt.show()

def main():
  if len(sys.argv) != 2:
    print('Usage: %s [dataset_train.csv]' % (sys.argv[0]))
    sys.exit(1)

  df = utils.get_data(sys.argv[1])
  courts = [elem for elem in df.columns.values.tolist() 
  if elem not in [HOUSES_COL, 'First Name', 'Last Name', 'Birthday', 'Best Hand']]

  for court in courts:
    plot_hist(court, df)

if __name__ == "__main__":
  main()