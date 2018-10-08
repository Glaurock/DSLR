# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logreg_predict.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmonnier <gmonnier@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/08 13:20:29 by gmonnier          #+#    #+#              #
#    Updated: 2018/10/08 13:20:29 by gmonnier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import sys
import numpy as np

import utils
from OneForAll import OneForAll

def main():
    if len(sys.argv) != 3:
        print('Usage: %s [dataset_test.csv] [.parameters.json]' % (sys.argv[0]))
        sys.exit(1)

    df = utils.get_data(sys.argv[1])
    df = df[utils.SELECTED_FEATURES + [utils.HOUSES_COL]]
    df.fillna(0, inplace=True)

    X = df[utils.SELECTED_FEATURES]

    oneForAll = OneForAll()
    oneForAll.load_parameters(sys.argv[2])
    oneForAll.predict(X)
    oneForAll.save_to_csv('houses.csv')

if __name__ == "__main__":
    main()