Koji package monitor
====================

Monitor `koji <http://koji.fedoraproject.org>`_, for packages completing build.

Running
-------

.. code-block:: bash

   sudo yum install fedmsg-hub
   sudo cp config.py /etc/fedmsg.d/kojipackagemonitor.py
   python setup.py egg_info
   PYTHONPATH=$(pwd) fedmsg-hub


Thanks
------

Adapted from https://github.com/lmacken/fedmsg-koji-consumer

