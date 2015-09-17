Quick demo of pip's editable mode
=================================

Whe you ``pip install -e .`` a project, it creates a .egg-link file in
the ``site-package`` directory which basically contains a link to your
local development directory which has the ``.egg-info`` directory.
(See
http://svn.python.org/projects/sandbox/trunk/setuptools/doc/formats.txt
to learn more about egg links)

Demo
----

- Run ``pip install -e .``
- You will find a ``sample.egg-link`` file in your ``site-packages``
  directory
- It will contain the local development directory on one line and the
  second line will consist of a ``.`` (relative path of the egg's base
  directory to the ``setup.py`` file.
- Now run, ``hello`` from your terminal, it will print ``Hello
  called``. Now, modify the ``hello`` module to return something
  else. Executing the ``hello`` command again will print the new
  message now.
