#!/bin/bash

oz-install -p -u -d3 -a fedora22.ks fedora22.tdl
#qemu-img convert /var/lib/libvirt/images/fedora22_x86_64.dsk -O qcow2 fedora22_x86_64.qcow2
#./create_box.sh fedora22_x86_64.qcow2
