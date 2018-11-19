# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logreg_train.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmonnier <gmonnier@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/08 13:20:41 by gmonnier          #+#    #+#              #
#    Updated: 2018/11/19 13:43:15 by gmonnier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt
import plac

import utils
from OneForAll import OneForAll

@plac.annotations(
    dataset = plac.Annotation("dataset_train.csv from resources",'positional'),
    plotLoss = plac.Annotation("Plot loss curves for each logistic regression", "flag", 'p'),
    verbose = plac.Annotation("Print loss in learning", "flag", "v"),
    scatter = plac.Annotation("Plot the prediction in learning", "flag", "s"),
    alpha = plac.Annotation('Set the learning rate', 'option', 'l', float),
    n_epoch = plac.Annotation('Set the number of epochs', 'option', 'e', int),
)
def main(dataset, plotLoss, verbose, scatter, alpha, n_epoch):
    try:
        df = utils.get_data(sys.argv[1])
        df = df[utils.SELECTED_FEATURES + [utils.HOUSES_COL]]
        df.dropna(inplace=True) 
    except Exception as e:
        print("Error parsing input file, is it valid?")
        sys.exit(1)

    msk = np.random.rand(len(df)) < 0.75
    train = df[msk]
    test = df[~msk]

    df = train
    print(df.shape)
    print(train.shape)
    print(test.shape)

    ## create 1 or 0 for each class for one versus all 
   # Y_list = {}
    #for house in utils.HOUSES:
        #Y_list[house] = (np.array([1 if elem == house else 0
            #for elem in df[utils.HOUSES_COL]]))
    #X = df[utils.SELECTED_FEATURES]

    #oneForAll = OneForAll(verbose, plotLoss, scatter)
    #oneForAll.fit(X, Y_list, alpha, n_epoch)
    #oneForAll.save_parameters()

    #if plotLoss:
   #     oneForAll.plot_all_loss_curves()

    ##
    test.reset_index(inplace=True)
    a = OneForAll()
    a.load_parameters(".parameters.json")
    a.predict(test[utils.SELECTED_FEATURES])
    a.save_to_csv('houses.csv')
    
    res = pd.read_csv('houses.csv', index_col=0)
    res['test'] = test[utils.HOUSES_COL]
    res2 = res['test'] == res[utils.HOUSES_COL]
    print(np.sum(res2) / len(res2))
    ##

if __name__ == "__main__":
    plac.call(main)
