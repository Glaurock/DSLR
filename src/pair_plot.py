# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pair_plot.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmonnier <gmonnier@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/08 13:21:17 by gmonnier          #+#    #+#              #
#    Updated: 2018/11/17 15:45:36 by gmonnier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import sys

import utils

def cut_col(df):
    df.columns = [utils.cut_str(col) for col in df.columns.values]
    return df

def main():
    if len(sys.argv) != 2:
        print('Usage: %s [dataset_train.csv]' % (sys.argv[0]))
        sys.exit(1)

    try:
        df = utils.get_data(sys.argv[1])
        df = df.fillna(0)
        df = cut_col(df)
        sns.pairplot(df, hue=utils.cut_str(utils.HOUSES_COL), dropna=True, plot_kws={"s": 6}, height=1.75)
        plt.tight_layout()
        plt.subplots_adjust(
                left=0.04,
                bottom=0.07,
                right=0.92,
                top=0.99,
                wspace=0.52,
                hspace=0.71)
        plt.show()
    except Exception as e:
        print(e)
        print("Error trying to plot the pair plot")
        sys.exit(1)
    ## Herbology, Astronomy, Defense against dark
    ## left 0.04 bottom 0.07 right 0.92 top 0.99 wspace 0.52 hspace 0.71


if __name__ == "__main__":
  main()
