#!/usr/bin/env bash
set -euox pipefail

apt-get update
apt-get install git -y

cd ~
cp /local_fwego_repo/docs/guides/installation/old-install-on-ubuntu.md install-on-ubuntu.md

# Process the guide to only extract the bash we want
sed -n '/## HTTPS \/ SSL Support/q;p' install-on-ubuntu.md | # We don't want to setup https or do any upgrade scripts which follow
sed -n '/^```bash$/,/^```$/p' | # Extract bash code from markdown code blocks
sed '/^```/ d' | # Get rid of the backticks left in by the previous sed
sed 's/^\$ //' | # Get rid of the bash command $ prefixes
sed 's/^sudo passwd fwego/echo -e "yourpassword\nyourpassword" | sudo passwd fwego/' | # Enter a password non interactively
sed "s/git clone --branch master.*/cp -r \/local_fwego_repo fwego/" | # Copy your local repo over instead of checking out master
sed 's/https:\\\/\\\/api.domain.com/http:\\\/\\\/api.fwego.vagrant.test/g' | # Fixup the sed commands for the URL env vars
sed 's/https:\\\/\\\/fwego.domain.com/http:\\\/\\\/fwego.vagrant.test/g' |
sed 's/https:\\\/\\\/media.domain.com/http:\\\/\\\/media.fwego.vagrant.test/g' |
sed 's/api.domain.com/api.fwego.vagrant.test/g' | # Fixup the sed commands for the nginx config
sed 's/fwego.domain.com/fwego.vagrant.test/g' |
sed 's/media.domain.com/media.fwego.vagrant.test/g' > install-on-ubuntu.sh

# Prepend with some bash settings so we can see the output and it will fail if something
# crashes.
# We dont set -u here due to problems with it using an old virtualenv and PS1 not being
# set. See https://stackoverflow.com/questions/42997258/virtualenv-activate-script-wont-run-in-bash-script-with-set-euo
echo -e "set -eox pipefail\n$(cat install-on-ubuntu.sh)" > install-on-ubuntu.sh

# TODO Figure out the right sudo su incantation to run this as a normal user with sudo
bash install-on-ubuntu.sh
