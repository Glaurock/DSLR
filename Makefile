# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmonnier <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/11/17 12:53:46 by gmonnier          #+#    #+#              #
#    Updated: 2018/11/19 11:52:02 by gmonnier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

all: install

install:
	pip3 install -r requirements.txt

describe:
	python3 src/describe.py ./resources/dataset_train.csv

histogram:
	python3 src/histogram.py ./resources/dataset_train.csv

scatterplot:
	python3 src/scatter_plot.py ./resources/dataset_train.csv

pairplot:
	python3 src/pair_plot.py ./resources/dataset_train.csv

train:
	python3 src/logreg_train.py ./resources/dataset_train.csv

predict:
	python3 src/logreg_predict.py ./resources/dataset_test.csv .parameters.json

clean:
	rm .parameters.json
	rm houses.csv
	rm -rf __pycache__
	rm -rf src/__pycache__/
