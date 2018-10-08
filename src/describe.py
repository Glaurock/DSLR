# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    describe.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmonnier <gmonnier@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/08 13:20:48 by gmonnier          #+#    #+#              #
#    Updated: 2018/10/08 13:20:48 by gmonnier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import csv
import math
import numpy as np
import pandas as pd
import utils

def ft_delete(data):
  for col in data:
    if not utils.is_number(data[col][0]):
      del data[col]
  return data

def main():
  if len(sys.argv) != 2:
    print('Usage: %s [dataset.csv]' % (sys.argv[0]))
    sys.exit(1)

  data = utils.get_data(sys.argv[1])
  data = ft_delete(data)
  result = pd.DataFrame(index=["Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"], columns=data.columns.values)

  for col in data:
    result[col] = utils.ft_calc(data[col])
  # result = result.astype(dtype='float64')
  
  print(result)

if __name__ == "__main__":
  main()