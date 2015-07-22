import tempfile
import os
import subprocess

fd, name = tempfile.mkstemp()
os.write(fd, "# Create your changelog entry below:\n")
editor = 'vi'
if "EDITOR" in os.environ:
	editor = os.environ["EDITOR"]
        subprocess.call(editor.split() + [name])

       	os.lseek(fd, 0, 0)
        file = os.fdopen(fd)
        output = file.read()
	file.close()
        os.unlink(name)
	print output
