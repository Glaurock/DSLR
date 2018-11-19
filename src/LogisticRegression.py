# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    LogisticRegression.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmonnier <gmonnier@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/08 13:20:58 by gmonnier          #+#    #+#              #
#    Updated: 2018/11/19 12:14:46 by gmonnier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class LogisticRegression:
    def __init__(self, class_name, lr=0.01, num_iter=10000,
    fit_intercept=True, verbose=False, normalize=True, plot=False, scatter=False):
        self.lr = lr if lr is not None else 0.01
        self.num_iter = num_iter if num_iter is not None else 100000
        self.fit_intercept = fit_intercept
        self.verbose = verbose
        self.normalize = normalize
        self.class_name = class_name
        self.loss_curve = []
        self.plot = plot
        self.scatter = scatter
        
    def __normalize(self, x):
        return (x - x.min()) / (x.max() - x.min())

    def __denormalize(self, x):
        return x * (x.max() - x.min()) + x.min()
    
    def __add_intercept(self, X):
        intercept = np.ones((X.shape[0], 1))
        return np.concatenate((intercept, X), axis=1)
    
    def __sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def __loss(self, h, y):
        return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()
    
    def __compute_gradient(self, X, y, h):
        return np.dot(X.T, (h - y)) / y.size
    
    def fit(self, X, y):
        print("Fit parameters...")
        if self.normalize:
            X = self.__normalize(X)
        
        if self.fit_intercept:
            X = self.__add_intercept(X)
        
        # weights initialization
        self.theta = np.zeros(X.shape[1])
        
        for i in range(self.num_iter):
            z = np.dot(X, self.theta)
            h = self.__sigmoid(z)
            gradient = np.dot(X.T, (h - y)) / y.size
            self.theta -= self.lr * gradient

            if self.plot:
                z = np.dot(X, self.theta)
                h = self.__sigmoid(z)
                self.loss_curve.append(self.__loss(h, y))

            if(self.verbose == True and i % (self.num_iter / 10) == 0):
                z = np.dot(X, self.theta)
                h = self.__sigmoid(z)
                print(f'loss: {self.__loss(h, y)} \t')

            if (self.scatter and i % (self.num_iter / 10) == 0):
                y_pred = self.predict(X[:,1:])
                plt.scatter(X[:,1], X[:,2],c=y_pred)
                plt.show(block=False)
                plt.pause(1)
                plt.close()

    def predict_prob(self, X):
            if self.normalize:
                X = self.__normalize(X)
            if self.fit_intercept:
                X = self.__add_intercept(X)
            ret = self.__sigmoid(np.dot(X, self.theta))
            ret = self.__denormalize(ret)
            return ret
    
    def predict(self, X, threshold=0.75):
        if self.normalize:
            X = self.__normalize(X)
        return self.predict_prob(X) >= threshold

