#!/bin/bash
set -e

start_nfs() {
    exportfs -a
    rpcbind
    rpc.statd
    rpc.nfsd
}

start_nfs
exec rpc.mountd --foreground