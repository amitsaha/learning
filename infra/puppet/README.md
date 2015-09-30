###Puppet

- Following along from Puppet courseware learning VM: https://github.com/puppetlabs/courseware-lvm

- Resource, manifests, modules: https://docs.puppetlabs.com/pe/latest/puppet_modules_manifests.html
- Commands: ``puppet parser validate``, ``puppet apply``, ``puppet master --configprint modulepath``, ``puppet resource service ntpd``
- /etc/puppetlabs/puppet/manifests/site.pp is the main entry point used when an agent connects to a master and asks   for an updated configuration.

```
node default {
    include ntp
    }
```

Passing class parameters:

```
node default {
  class { 'ntp':
      servers =>
            ['nist-time-server.eoni.com','nist1-lv.ustiming.org','ntp-nist.ldsbc.edu']
            }
            
            }
            ```

- Modules can define custom resources and types. For example the puppet-mysql module
(https://forge.puppetlabs.com/puppetlabs/mysql#mysql_database)

- Example of site.pp configuring mysql in this directory

- Variables and class parameters - class parameters allow specifying variables when
  declaring then while defining them (See ``web/`` for an example)

- ``facter``: Collect and display facts about the system

- Resource relationships and ordering, see ``sshd/``

- Modules with sub-directories in manifests, see ``modules-with-directories``
