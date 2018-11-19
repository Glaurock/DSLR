# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scatter_plot.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmonnier <gmonnier@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/08 13:21:20 by gmonnier          #+#    #+#              #
#    Updated: 2018/11/19 12:01:08 by gmonnier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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
    try:
        df = utils.get_data(sys.argv[1])
        features = [elem for elem in df.columns.values.tolist() 
        if elem not in [utils.HOUSES_COL, 'First Name', 'Last Name', 'Birthday', 'Best Hand']]
    except Exception as e:
        print("Error parsing input file, is it valid?")
        sys.exit(1)

    comb = list(itertools.combinations(features, 2)) 
    i = 1
    fig = plt.figure(figsize=(20,14))
    for x_name, y_name in comb:
        ax = fig.add_subplot(9, 9, i)
        x = df[x_name]
        y = df[y_name]
        _ = ax.scatter(x, y, s=0.25)
        ax.set_xlabel(utils.cut_str(x_name), fontsize=10)
        ax.set_ylabel(utils.cut_str(y_name))
        i += 1
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
  main()
