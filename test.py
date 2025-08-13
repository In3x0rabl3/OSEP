#!/usr/bin/env python3
import os
import time
from pyverbs.device import Context, DeviceList
from pyverbs.pd import PD
from pyverbs.cq import CQ
from pyverbs.qp import QP, QPInitAttr, QPCap
from pyverbs.mr import MR

# Simple check: list available RDMA devices in this pod
def list_rdma_devices():
    dev_list = DeviceList()
    print("[*] Available RDMA devices:")
    for dev in dev_list:
        print(f"    - {dev.name.decode()} ({dev.dev_name.decode()})")

# Create and expose a buffer to test shared access
def allocate_and_write(ctx):
    pd = PD(ctx)
    cq = CQ(ctx, 10, None, None, 0)
    cap = QPCap(max_send_wr=10, max_recv_wr=10, max_send_sge=1, max_recv_sge=1)
    qp_init_attr = QPInitAttr(qp_type=2, scq=cq, rcq=cq, cap=cap)
    qp = QP(pd, qp_init_attr)
    mr = MR(pd, 4096, 7)  # Permissions: LocalWrite | RemoteWrite | RemoteRead
    buf = mr.buf
    buf[:len(b"HELLO_FROM_SENDER")] = b"HELLO_FROM_SENDER"
    print("[*] Wrote test string into RDMA buffer.")
    return mr

def main():
    list_rdma_devices()

    # Open first RDMA device context
    dev_list = DeviceList()
    if not dev_list:
        print("[!] No RDMA devices found in this pod.")
        return
    ctx = Context(name=dev_list[0].name)

    mr = allocate_and_write(ctx)
    print("[*] Memory region key:", mr.rkey)
    print("[*] Memory region address:", hex(mr.buf.__array_interface__['data'][0]))

    print("[*] Share this rkey and address to another pod to attempt unauthorized read.")

if __name__ == "__main__":
    main()
