# ==============================================================================
# Tensorflow Cobra framework
# Author Yan Feng
# Build for general Tensorflow Data imports from local dir
# 2017/3/3:implementation of gzip data import
# ==============================================================================
"""Functions for general data importing."""

import gzip
import numpy
import os
from tensorflow.contrib.learn.python.learn.datasets import base
from tensorflow.python.framework import dtypes

exp_local_dir = "D:\\train\\"


class CobraDataSet(object):

    def __init__(self,
                 local_dir,
                 filetype,

                 ):
        self.local_dir = local_dir
        self.filetype = filetype

    def return_filelist(self):
        filelist = []
        for root, dirs, files in os.walk(self.local_dir):
            for name in files:
                if
                filelist.append(os.path.join(root, name))
        return filelist

    def return_



dataset1 = CobraDataSet(exp_local_dir,"gz")
print(dataset1.return_filelist())









