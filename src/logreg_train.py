import pandas as pd
import sys
import numpy as np

import utils
from OneForAll import OneForAll

def main():
    if len(sys.argv) != 2:
        print('Usage: %s [dataset_train.csv]' % (sys.argv[0]))
        sys.exit(1)

    df = utils.get_data(sys.argv[1])
    df = df[['Hogwarts House', 'Astronomy', 'Herbology']]
    df.dropna(inplace=True) 
    
    ## create 1 or 0 for each class for one versus all 
    Y_list = {}
    for house in utils.HOUSES:
        Y_list[house] = (np.array([1 if elem == house else 0 for elem in df[utils.HOUSES_COL]]))
    X = df[['Astronomy', 'Herbology']]

    oneForAll = OneForAll()
    oneForAll.fit(X, Y_list, True)
    oneForAll.save_parameters()

if __name__ == "__main__":
    main()