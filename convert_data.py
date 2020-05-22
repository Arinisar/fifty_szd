import  numpy as np
import os.path

data = np.load(os.path.abspath('./512_1/512_1/test.npz'))
data_frags = data['x']

print(np.shape(data_frags))
newshape_data = 204800*512
data_frags = np.reshape(data_frags, (newshape_data))
print(np.shape(data_frags))
data_frags = bytes(data_frags)
outfile = open("outfile.bin", 'wb')
outfile.write(data_frags)
