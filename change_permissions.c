#define _GNU_SOURCE
#include <unistd.h>
#include <sys/mman.h>
#include <stdint.h>

int change_page_permissions_of_address(uintptr_t addr) {
    int page_size = getpagesize();
    addr -= addr % page_size;

    if(mprotect((void*)addr, page_size, PROT_READ | PROT_WRITE | PROT_EXEC) == -1) {
        return -1;
    }

    return 0;
}
