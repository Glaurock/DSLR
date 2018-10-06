import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import itertools
import sys

import utils

HOUSES_COL = 'Hogwarts House'

def main():
    if len(sys.argv) != 2:
        print('Usage: %s [dataset_train.csv]' % (sys.argv[0]))
        sys.exit(1)

    df = utils.get_data(sys.argv[1])
    features = [elem for elem in df.columns.values.tolist() 
    if elem not in [HOUSES_COL, 'First Name', 'Last Name', 'Birthday', 'Best Hand']]

    comb = list(itertools.combinations(features, 2)) 
    for x_name, y_name in comb:
        x = df[x_name]
        y = df[y_name]
        _ = plt.scatter(x, y)
        plt.xlabel(x_name)
        plt.ylabel(y_name)
        plt.show()

if __name__ == "__main__":
  main()
