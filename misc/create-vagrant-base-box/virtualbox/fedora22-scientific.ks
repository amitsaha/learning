# Kickstart for Fedora Scientific vagrant box
# Borrows ideas from official Fedora vagrant box kickstart and
# the packages, etc from Fedora Scientific Kickstart

install
text
keyboard us
lang en_US.UTF-8
network --device eth0 --bootproto dhcp
rootpw changeme
firewall --disabled

repo --name="fedora" --mirrorlist=http://mirrors.fedoraproject.org/metalink?repo=fedora-22&arch=$basearch
repo --name="updates" --mirrorlist=http://mirrors.fedoraproject.org/metalink?repo=updates-released-f22&arch=$basearch

authconfig --enableshadow --enablemd5

# X Window System configuration information
xconfig  --startxonboot --defaultdesktop=KDE

selinux --enforcing
timezone --utc Australia/Brisbane

bootloader --timeout=1 --append="no_timer_check console=tty1 console=ttyS0,115200n8 net.ifnames=0 biosdevname=0" --extlinux
clearpart --all

part /boot --fstype ext4 --size=200
part swap --size=512
part / --fstype ext4 --size=12288 --grow

user --name=vagrant --password=vagrant --plaintext
rootpw vagrant --plaintext


reboot


%packages
@anaconda-tools
@base-x
@c-development
@core
@development-libs
@development-tools
@dial-up
@eclipse
@engineering-and-scientific
@fonts
@guest-desktop-agents
@hardware-support
@input-methods
@java-development
@kde-apps
@kde-desktop
@kde-education
@kde-media
@kde-office
@kde-telepathy
@multimedia
@networkmanager-submodules
@printing
@rpm-development-tools
@standard
BibTool
Mayavi
aajohan-comfortaa-fonts
anaconda
apache-commons-math
armadillo-devel
backintime-kde
bibtex2html
blitz-devel
cantor-R
ddd
dia
emacs
emacs-color-theme
fig2ps
firefox
fuse
g3data
gcc-gfortran
ggobi
ggobi-devel
gimp
git
git-gui
hevea
hexchat
inkscape
k3b
kde-l10n
kde-wallpapers
kernel
kile
krusader
libgomp
libotf
liveusb-creator
lyx
mariadb-embedded
mariadb-libs
mariadb-server
maxima
memtest86+
mercurial
mercurial-hgk
mpi4py-openmpi
octave
openmpi
openmpi-devel
pdfshuffler
pvm
pvm-gui
python-ipython
python-ipython-console
python-ipython-notebook
python-matplotlib-qt4
python-matplotlib-tk
python-networkx
python-pandas
python-pp
python-tools
python3
python3-ipython
python3-ipython-console
python3-ipython-notebook
python3-matplotlib
python3-matplotlib-qt4
python3-matplotlib-tk
python3-mpi4py-openmpi
python3-networkx
python3-numpy
python3-pandas
python3-scipy
python3-sympy
python3-tools
qtoctave
rapidsvn
rkward
rlwrap
root
root-gui-fitpanel
root-python
scilab
scilab-devel
scilab-doc
screen
scribus
shutter
spyder
sympy
system-config-language
tmux
valgrind
valgrind-openmpi
vim
xzgv
-autofs
-calligra-l10n-*
-coolkey
-desktop-backgrounds-basic
-hpijs
-hplip
-isdn4k-utils
-kde-l10n-*
-mpage
-numactl
-sane-backends
-sox
-system-config-printer
-wget
-xsane
-xsane-gimp

%end
