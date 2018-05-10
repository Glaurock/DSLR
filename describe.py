import sys
import csv
import math
import numpy as np
import pandas as pd

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

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

def ft_std(col, mean, count):
  a = 0

  for val in col:
    if val:
      a += (float(val) - mean) * (float(val) - mean)
  a /= count
  a = math.sqrt(a)
  return a

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

def ft_delete(data):
  for col in data:
    if not is_number(data[col][0]):
      del data[col]
  return data

def main():
  if len(sys.argv) != 2:
    print('Usage: %s [dataset.csv]' % (sys.argv[0]))
    sys.exit(1)

  data = get_data(sys.argv[1])
  data = ft_delete(data)
  result = pd.DataFrame(index=["Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"], columns=data.columns.values)

  for col in data:
    result[col] = ft_calc(data[col])
  result = result.astype(dtype='float64')
  
  print(result)

if __name__ == "__main__":
  main()