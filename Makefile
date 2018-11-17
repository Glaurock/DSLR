# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmonnier <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/11/17 12:53:46 by gmonnier          #+#    #+#              #
#    Updated: 2018/11/17 13:22:13 by gmonnier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

all:
	pip3 install -r requirements.txt

describe:
	python3 src/describe.py ./resources/dataset_train.csv

histogram:
	python3 src/histogram.py ./resources/dataset_train.csv

scatterplot:
	python3 src/scatter_plot.py ./resources/dataset_train.csv

clean:
	rm -rf __pycache__
	rm -rf src/__pycache__/
