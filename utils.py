import math
import sys
import csv
import pandas as pd

def ft_std(col, mean, count):
  a = 0

  for val in col:
    if val:
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
  # col = col.replace('', np.nan)
  sorted_list = col.sort_values()
  q1 = sorted_list.iloc[q1]
  q2 = sorted_list.iloc[q2]
  q3 = sorted_list.iloc[q3]
  # print(sorted_list)
  
  return [q1, q2, q3]

def ft_calc(col):
  count = 0
  tot = 0
  minimum = col[0]
  maximum = col[0]

  for val in col:
    if val:
      tot += float(val)
      count += 1
      if val < minimum:
       minimum = val
      if val > maximum:
        maximum = val

  mean = tot / count
  std = ft_std(col, mean, count)
  q1, q2, q3 = ft_quartiles(col, count)
  return [count, mean, std, minimum, q1, q2, q3, maximum]

def get_data(argv):
  try:
    with open(argv, 'rt') as csvfile:
      base_data = csv.reader(csvfile, delimiter=',')
      list_data = [x for x in base_data]
      data = pd.DataFrame(data=list_data[1:], columns=list_data[0])
  except Exception as e:
    print(e)
    sys.exit(1)
  
  return data