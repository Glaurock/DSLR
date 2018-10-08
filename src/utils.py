# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmonnier <gmonnier@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/08 13:20:36 by gmonnier          #+#    #+#              #
#    Updated: 2018/10/08 13:20:37 by gmonnier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math
import sys
import csv
import pandas as pd
import numpy as np

HOUSES_COL = 'Hogwarts House'
HOUSES = ["Ravenclaw", "Slytherin", 'Gryffindor', "Hufflepuff"]
SELECTED_FEATURES = ['Astronomy', 'Herbology', 'Charms', 'Flying']

def ft_std(col, mean, count):
    a = 0

    for val in col:
        if not np.isnan(val):
            a += (float(val) - mean) * (float(val) - mean)
    a /= count
    a = math.sqrt(a)
    return a

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def ft_quartiles(col, count):
    q1 = int(math.ceil(count * 0.25))
    q2 = int(math.ceil(count * 0.5))
    q3 = int(math.ceil(count * 0.75))
    sorted_list = col.sort_values()
    q1 = sorted_list.iloc[q1]
    q2 = sorted_list.iloc[q2]
    q3 = sorted_list.iloc[q3]
  
    return [q1, q2, q3]


def ft_calc(col):
    count = 0
    tot = 0
    minimum = col[0]
    maximum = col[0]

    for val in col:
        if not np.isnan(val):
            tot += float(val)
            count += 1
            if val < minimum:
                minimum = val
            if val > maximum:
                maximum = val

    if (count > 0):
        mean = tot / count
        std = ft_std(col, mean, count)
        q1, q2, q3 = ft_quartiles(col, count)
        return [count, mean, std, minimum, q1, q2, q3, maximum]
    return [0, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan] 

def get_data(argv):
  try:
    df = pd.read_csv(argv, index_col=0)
    return df
  except Exception as e:
    print(e)
    sys.exit(1)
  
  return data