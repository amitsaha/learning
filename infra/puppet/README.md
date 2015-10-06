# Setup

- http://echorand.me/standalone-open-source-puppet-setup-on-fedora.html#.Vg4jo3VStBc

# Writing your Modules

## References

- Defining your own classes: https://docs.puppetlabs.com/puppet/latest/reference/lang_classes.html#defining-classes
- Defined resource types: https://docs.puppetlabs.com/puppet/4.2/reference/lang_defined_types.html
- https://docs.puppetlabs.com/puppet/latest/reference/modules_fundamentals.html
- https://docs.puppetlabs.com/puppet/latest/reference/lang_defined_types.html
- https://docs.puppetlabs.com/puppet/latest/reference/lang_resources.html
- Puppet function reference: https://docs.puppetlabs.com/references/latest/function.html#function-reference
- Puppet language data types: https://docs.puppetlabs.com/puppet/latest/reference/lang_data_number.html#language:-data-types:-numbers


## Notes


Use ``puppet module generate amitsaha-classdefineexample`` to generate a module template



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
