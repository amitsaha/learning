#!/usr/bin/env bash
set -e
cat > metadata.json <<EOF
{
    "provider": "virtualbox",
}
EOF

cat > Vagrantfile <<EOF

Vagrant.configure("2") do |config|
  config.vm.base_mac = "525400c64cfc"
  config.vm.synced_folder ".", "/vagrant", type: "rsync"
end

EOF

BOX="Fedora22_x86_64_scientific.box"
echo "==> Creating box, tarring and gzipping"
tar cvzf $BOX --totals ./box.ovf ./metadata.json ./Vagrantfile ./fedora22_x86_64_scientific.vmdk

echo "==> ${BOX} created"
echo "==> You can now add the box:"
echo "==>   'vagrant box add ${BOX} --name ${BOX_NAME}'"
