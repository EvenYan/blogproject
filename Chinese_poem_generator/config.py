# coding: UTF-8

import tensorflow as tf
import numpy as np
import argparse
import os
import random
import time
import collections

batchSize = 64

learningRateBase = 0.001
learningRateDecayStep = 1000
learningRateDecayRate = 0.95

epochNum = 10                    # train epoch
generateNum = 5                   # number of generated poems per time

type = "poetrySong"                   # dataset to use, shijing, songci, etc
trainPoems = "/home/even/PycharmProjects/blog/blogproject/Chinese_poem_generator/dataset/" + type + "/" + type + ".txt" # training file location
checkpointsPath = "/home/even/PycharmProjects/blog/blogproject/Chinese_poem_generator/checkpoints/" + type # checkpoints location

saveStep = 1000                   # save model every savestep



# evaluate
trainRatio = 0.8                    # train percentage
evaluateCheckpointsPath = "/home/even/PycharmProjects/blog/blogproject/Chinese_poem_generator/checkpoints/evaluate"
