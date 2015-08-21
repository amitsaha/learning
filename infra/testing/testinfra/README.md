README
======

Simple tests using ``testinfra``
(https://testinfra.readthedocs.org/). To run the tests, install
``testinfra`` using ``pip`` and execute the command ``testinfra
-v``.

Examples
--------

*Run locally*

By defaultt, ``testinfra`` will run the tests on your host system.

*Run tests in a running container*

```
$ testinfra -v --connection=docker --hosts=dreamy_einstein
```

*Run tests on a different host*

This can be done via the ``paramiko`` or ``ssh`` backends
(https://testinfra.readthedocs.org/en/latest/backends.html)

testinfra has a number of other modules: https://testinfra.readthedocs.org/en/latest/modules.html