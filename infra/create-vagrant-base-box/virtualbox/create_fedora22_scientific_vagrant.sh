#!/bin/bash

oz-install -p -u -d3 -a fedora22-scientific.ks fedora22-scientific.tdl
qemu-img convert /var/lib/libvirt/images/fedora22_x86_64_scientific.dsk -O vmdk fedora22_x86_64_scientific.vmdk
./create_box.sh
