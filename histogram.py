import utils
import matplotlib.pyplot as plt
import pandas as pd
import sys

def main():
 if len(sys.argv) != 2:
    print('Usage: %s [dataset.csv]' % (sys.argv[0]))
    sys.exit(1)

data = utils.get_data(sys.argv[1])

data = data[data['Hogwarts House'] == 'Ravenclaw']
print(data)

if __name__ == "__main__":
  main()