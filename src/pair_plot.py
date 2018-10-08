# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pair_plot.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmonnier <gmonnier@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/08 13:21:17 by gmonnier          #+#    #+#              #
#    Updated: 2018/10/08 13:21:18 by gmonnier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
# import numpy as np
# import itertools
import sys

import utils

HOUSES_COL = 'Hogwarts House'

def main():
    if len(sys.argv) != 2:
        print('Usage: %s [dataset_train.csv]' % (sys.argv[0]))
        sys.exit(1)

    df = utils.get_data(sys.argv[1])
    df = df.fillna(0)
    sns.pairplot(df, hue=HOUSES_COL, dropna=True, plot_kws={"s": 6}, height=2.5)
    plt.show()
    ## Herbology, Astronomy, Defense against dark

if __name__ == "__main__":
  main()
