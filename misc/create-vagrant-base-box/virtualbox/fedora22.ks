install
text
keyboard us
lang en_US.UTF-8
skipx
network --device eth0 --bootproto dhcp
rootpw changeme
firewall --disabled
authconfig --enableshadow --enablemd5
selinux --enforcing
timezone --utc Asia/Singapore
bootloader --location=mbr --append="console=tty0 console=ttyS0,115200"
clearpart --all

part /boot --fstype ext4 --size=200
part swap --size=512
part / --fstype ext4 --size=1024 --grow

user --name test --password changeme --plaintext --groups wheel

reboot

%packages
@core
python3

%end
