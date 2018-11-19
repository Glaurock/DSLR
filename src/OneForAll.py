# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    OneForAll.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmonnier <gmonnier@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/08 13:21:13 by gmonnier          #+#    #+#              #
#    Updated: 2018/11/19 13:46:24 by gmonnier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import operator
import pandas as pd
import numpy as np
from itertools import combinations
import json
import sys
import matplotlib.pyplot as plt

import utils
from LogisticRegression import LogisticRegression

class OneForAll:
    def __init__(self, verbose=False, plot=False, scatter=False):
        self.log_list = []
        self.probas = []
        self.verbose = verbose
        self.plot = plot
        self.scatter = scatter

    def __get_index_max_proba(self, a):
        index, value = max(enumerate(a), key=operator.itemgetter(1))
        try:
            ret = self.log_list[index].class_name
            return ret
        except e as Exception:
            print(e)
            
    def __get_highest_proba(self):
        self.res = []
        for a in list(zip(self.probas[0], self.probas[1],
            self.probas[2], self.probas[3])):
            self.res.append(self.__get_index_max_proba(a))
            
    def fit(self, X, Y_list, alpha, n_epoch):
        for key, Y in Y_list.items():
            log = LogisticRegression(key, verbose=self.verbose, plot=self.plot, scatter=self.scatter, lr=alpha, num_iter=n_epoch)
            log.fit(X, Y)
            self.log_list.append(log)
            
    def save_parameters(self):
        save = {}
        for log in self.log_list:
            save[log.class_name] = log.theta.tolist()
        with open('.parameters.json', 'w') as outfile:
            json.dump(save, outfile)
            print("Parameters save to '.parameters.json'")

    def load_parameters(self, file):
        try:
            with open(file, 'r') as f:
                data = json.load(f)
            for key, thetas in data.items():
                log = LogisticRegression(key)
                log.theta = np.array(thetas)
                self.log_list.append(log)
            print("Parameters loaded, ready to predict")
        except Exception as e:
            print(e)
            print("Error loading parameters, run or rerun learning first")
            sys.exit(1)


    def predict(self, X):
        for index, log in enumerate(self.log_list):
            ret = log.predict_prob(X)
            self.probas.append(ret)
        self.__get_highest_proba()
        
    ## add write index as col
    def save_to_csv(self, file):
        df = pd.DataFrame(self.res, columns=[utils.HOUSES_COL])
        df.to_csv(file)
        print("Predictions save to", file)

    ## just add legends
    def plot_all_loss_curves(self):
        x_axis = np.arange(0, self.log_list[0].num_iter)
        for log in self.log_list:
            plt.plot(x_axis, log.loss_curve)
        plt.xlabel("number of iteration")
        plt.ylabel("Loss")
        plt.title("Loss for each logistic regression")
        plt.show()
