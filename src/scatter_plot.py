# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scatter_plot.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmonnier <gmonnier@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/08 13:21:20 by gmonnier          #+#    #+#              #
#    Updated: 2018/10/08 14:18:18 by gmonnier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

##
#   Revoir le display des graphs comme pour histograms 
##

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import itertools
import sys

import utils

def main():
    if len(sys.argv) != 2:
        print('Usage: %s [dataset_train.csv]' % (sys.argv[0]))
        sys.exit(1)

    df = utils.get_data(sys.argv[1])
    features = [elem for elem in df.columns.values.tolist() 
    if elem not in [utils.HOUSES_COL, 'First Name', 'Last Name', 'Birthday', 'Best Hand']]

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
