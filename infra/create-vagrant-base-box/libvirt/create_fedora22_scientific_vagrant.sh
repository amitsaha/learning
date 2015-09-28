#!/bin/bash

oz-install -p -u -d3 -a fedora22-scientific.ks fedora22-scientific.tdl
qemu-img convert /var/lib/libvirt/images/fedora22_x86_64_scientific.dsk -O qcow2 fedora22_x86_64_scientific.qcow2
./create_box.sh fedora22_x86_64_scientific.qcow2
