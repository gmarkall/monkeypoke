import ctypes
import cupy as cp
from numba import cuda
import os

print(f"PID: {os.getpid()}")
get_pointer = ctypes.pythonapi.PyCapsule_GetPointer
get_pointer.argtypes = [ctypes.py_object, ctypes.c_char_p]
get_pointer.restype = ctypes.c_voidp

capsule = cp._core.core.__pyx_capi__['_convert_object_with_cuda_array_interface']
fptr = get_pointer(capsule, "struct __pyx_obj_4cupy_5_core_4core_ndarray *(PyObject *, int __pyx_skip_dispatch)".encode())

print("Function is at 0x%08x" % fptr)
input()

change_perms = ctypes.CDLL('change_permissions.so')
change_page_permissions_of_address = change_perms.change_page_permissions_of_address
change_page_permissions_of_address.argtypes = [ctypes.c_uint64]
change_page_permissions_of_address.restype = ctypes.c_int

res = change_page_permissions_of_address(fptr)
print(f"Result of changing address is... {res}")
input()


inst_ptr = ctypes.c_ushort.from_address(fptr)
old = inst_ptr.value
print(f"Old value is {old:x}")

ud2 = 0x0B0F
inst_ptr.value = ud2


print("Instruction patched... ?")
input()


nb_array = cuda.device_array(10)

cp.asarray(nb_array)
