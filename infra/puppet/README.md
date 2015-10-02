# Setup

- http://echorand.me/standalone-open-source-puppet-setup-on-fedora.html#.Vg4jo3VStBc

# Modules

It is not necessary to have a ``init.pp`` in your module. For example:

```
# tree test/
test/
└── manifests
    └── test1.pp

1 directory, 1 file

```
```
# cat test/manifests/test1.pp 
class test::test1 {

  file { '/etc/hostname': 
    ensure => 'file',    
  }
}
```

To include the ``test1`` class, we just include it in our manifest: 
```
include test::test1
```
