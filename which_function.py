import cupy as cp
from numba import cuda


nb_array = cuda.device_array(10)

cp.asarray(nb_array)
