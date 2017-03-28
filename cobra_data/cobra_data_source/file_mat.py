




import os
import scipy.io as sio
import h5py
import numpy as np


class MatFile(object):
    def __init__(self,
                 file_location,
                 file_version
                 ):
        self.file_location = file_location
        self.file_version = file_version
        self.__file = None

    def load_file(self):
        if self.file_version < 7.3:
            self.__file = sio.loadmat(self.file_location)
            print("Mat File Successfully Loaded(v7.2 or below)")
        else:
            self.__file = h5py.File(self.file_location)
            print("Mat File Successfully Loaded(v7.3 or above)")

    def conv_dic(self):
        f = self.__file
        data = f.get("digitStruct/bbox")
        data = np.array(data)
        ##strlist = [u''.join(chr(c) for c in obj_ref) for obj_ref in data]




        return data







file_location1="F:\\digitStruct.mat"
flie_version = 7.3
matrixname = "digitStruct"
matfile1 = MatFile(file_location1, flie_version)
matfile1.load_file()
print(matfile1.conv_dic())










