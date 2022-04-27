trampoline:
        call <Ashwin's function>
        push %r15
        push %r14
        push %r13
        push %r12
        ; Jump back to just past our jump-to-trampoline:
        jmp <_ZL68__pyx_f_4cupy...> + 8
