# Monkeypoke

Monkey-patching Cython extensions.

## Status

A given CuPy function can be patched with an undefined instruction.

Next steps:

- Add construction of trampoline functions
- Add an interface to specify the function called by the trampoline
- Add an interface to lookup arbitrary functions


## Building / running

To build the C chared library for changing memory page permissions, run:

```
gcc -fPIC -shared change_permissions.c -o change_permissions.so
```

You may need to add the current directory to `$LD_LIBRARY_PATH`.

Run the example with:

```
python patch_cupy.py
```

You should expect to see something like:

```
$ python patch_cupy.py 
PID: 1234333
Function is at 0x7f54ecdbd8f0

Result of changing address is... 0

Old value is 5741
Instruction patched... ?

Illegal instruction (core dumped)
```

You should be able to verify the patching in GDB by looking at a disassembly of
the function, e.g.:

```
Thread 1 "python" received signal SIGILL, Illegal instruction.
__pyx_f_4cupy_5_core_4core__convert_object_with_cuda_array_interface(...)
  at cupy/_core/core.cpp:45445
45445	cupy/_core/core.cpp: No such file or directory.
(gdb) disass
Dump of assembler code for function __pyx_f_4cupy_5_core_4core__convert_object_with_cuda_array_interface(PyObject*, int):
=> 0x00007fff9653a8f0 <+0>:	ud2
   0x00007fff9653a8f2 <+2>:	push   %r14
   0x00007fff9653a8f4 <+4>:	push   %r13
   0x00007fff9653a8f6 <+6>:	push   %r12
   0x00007fff9653a8f8 <+8>:	push   %rbp
   0x00007fff9653a8f9 <+9>:	push   %rbx
```
