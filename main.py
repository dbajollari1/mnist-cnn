import torch
import numpy as np 
import struct
import matplotlib.pyplot as plt


def main():
    with open('train/train-images.idx3-ubyte','rb') as f:
        data = f.read(8)
        print(struct.unpack(">II", data))
        # magic, size = struct.unpack(">II", f.read(8))
        # nrows, ncols = struct.unpack(">II", f.read(8))
        # data = np.fromfile(f, dtype=np.dtype(np.uint8).newbyteorder('>'))
        # data = data.reshape((size, nrows, ncols))

    
    # plt.imshow(data[0,:,:], cmap='gray')
    # plt.show()
 
    X_train = 0  #training data
    Y_train = 0  #training labels
    X_test = 0  #test data
    Y_test = 0  #test labels



if __name__ == "__main__":
    main()