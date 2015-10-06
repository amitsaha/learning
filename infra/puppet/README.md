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


### Parameterized Classes and Defined Resource types

Consider a class:

```
# cat classdefineexample/manifests/init.pp 
class classdefineexample ($command) {
  cron { $command:
    command => $command,
    user    => root,
    hour    => 3,
    minute  => 0
    }
}
```

If we want to use this class multiple times for different values of ``command``, we cannot:

```
class {'classdefineexample':
  command => 'command1'
}



# We can't do this any more

# class {'classdefineexample':
#   command => 'command2'
# }

# class {'classdefineexample':
#   command => 'command3'
# }

```

So, we must declare ``classdefineexample`` as a defined resource type:

```
define classdefineexample::cronjob($command) {
    cron { $command:
    command => $command,
    user    => root,
    hour    => 3,
    minute  => 0
    }
}

```

To Learn more:

- https://docs.puppetlabs.com/puppet/4.2/reference/lang_classes.html
- https://docs.puppetlabs.com/puppet/4.2/reference/lang_defined_types.html
- An [extract](https://books.google.com.au/books?id=VfBZAgAAQBAJ&pg=PA64&lpg=PA64&dq=puppet+class+singleton&source=bl&ots=S0IBWpnlg-&sig=-fl_hBgIe-shuSE39IDJ9QE1QlA&hl=en&sa=X&ved=0CE0Q6AEwCGoVChMI1dyj0LysyAIVxrqUCh3TAAkO#v=onepage&q=puppet%20class%20singleton&f=false) from Pro Puppet.



