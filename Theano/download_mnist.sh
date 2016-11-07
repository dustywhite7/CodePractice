#!/bin/bash

mkdir -p /home/dusty/CodePractice/Theano/mnist

if ! [ -e /home/dusty/CodePractice/Theano/mnist/train-images-idx3-ubyte.gz ]
	then
		wget -P /home/dusty/CodePractice/Theano/mnist/ http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
fi
gzip -d /home/dusty/CodePractice/Theano/mnist/train-images-idx3-ubyte.gz

if ! [ -e /home/dusty/CodePractice/Theano/mnist/train-labels-idx1-ubyte.gz ]
	then
		wget -P /home/dusty/CodePractice/Theano/mnist/ http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
fi
gzip -d /home/dusty/CodePractice/Theano/mnist/train-labels-idx1-ubyte.gz

if ! [ -e /home/dusty/CodePractice/Theano/mnist/t10k-images-idx3-ubyte.gz ]
	then
		wget -P /home/dusty/CodePractice/Theano/mnist/ http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
fi
gzip -d /home/dusty/CodePractice/Theano/mnist/t10k-images-idx3-ubyte.gz

if ! [ -e /home/dusty/CodePractice/Theano/mnist/t10k-labels-idx1-ubyte.gz ]
	then
		wget -P /home/dusty/CodePractice/Theano/mnist/ http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz
fi
gzip -d /home/dusty/CodePractice/Theano/mnist/t10k-labels-idx1-ubyte.gz
