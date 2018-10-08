# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    histogram.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmonnier <gmonnier@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/08 13:20:53 by gmonnier          #+#    #+#              #
#    Updated: 2018/10/08 14:17:40 by gmonnier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

##

##
## Revoir le display sur mac 
## Display une legend
##

##

import utils
import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np

BINS = 50

def plot_hist(court, df, fig, i):
    ar = df[[utils.HOUSES_COL, court]]
    ar_sort = ar.sort_values(court)
    ax = fig.add_subplot(4, 4, i)
    for house_name in utils.HOUSES:
        house = ar_sort.loc[ar_sort[utils.HOUSES_COL] == house_name]
        house = house[court].tolist()
        _ = ax.hist(house, bins=BINS, alpha=0.5, label=house_name)
    
    ax.set_ylabel('count')
    ax.set_xlabel('notes')
    ax.set_title(court)
    # ax.legend(loc='upper right')

def main():
  if len(sys.argv) != 2:
    print('Usage: %s [dataset_train.csv]' % (sys.argv[0]))
    sys.exit(1)

  df = utils.get_data(sys.argv[1])
  courts = [elem for elem in df.columns.values.tolist() 
  if elem not in [utils.HOUSES_COL, 'First Name', 'Last Name', 'Birthday', 'Best Hand']]

  i = 1
  fig = plt.figure()
  for court in courts:
      plot_hist(court, df, fig, i)
      i += 1
  plt.tight_layout()
  plt.show()

if __name__ == "__main__":
  main()