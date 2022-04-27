import ctypes
import cupy as cp

capsule_name = ("struct __pyx_obj_4cupy_5_core_4core_ndarray "
                "*(PyObject *, int __pyx_skip_dispatch)".encode())

get_pointer = ctypes.pythonapi.PyCapsule_GetPointer
get_pointer.argtypes = [ctypes.py_object, ctypes.c_char_p]
get_pointer.restype = ctypes.c_voidp

capsule = cp._core.core.__pyx_capi__['_convert_object_with_cuda_array_interface']
fptr = get_pointer(capsule, capsule_name)

print("Function is at 0x%08x" % fptr)
