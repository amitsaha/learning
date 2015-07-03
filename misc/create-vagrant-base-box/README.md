Creating a Vagrant Base box
===========================


## Steps for libvirt provider:

```
$ cd libvirt
# ./install_deps.sh
# ./create_fedora22_scientific_vagrant_libivrt.sh

(Needed to increase timeouts in Oz /usr/lib/python2.7/site-packages/oz/Guest.py
..more on this later)

```

## Steps for VirtualBox provider

# TODO

## Vagrant

```
# vagrant box add fedora22_x86_64_scientific.box --name Fedora22-scientific
# vagrant init Fedora22-scientific
# vagrant up
```


## With help from

# http://jansipke.nl/creating-a-centos-vm-image-for-openstack/
# https://github.com/pradels/vagrant-libvirt/
# https://blog.engineyard.com/2014/building-a-vagrant-box
