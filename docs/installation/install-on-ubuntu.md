# Installation on Ubuntu

> Any questions, problems or suggestions with this guide? Ask a question in our
> [community](https://community.fwego.io/) or contribute the change yourself at
> https://github.com/digitranslab/fwego/-/tree/develop/docs .

> If you installed Fwego 1.8.2 or earlier using this guide in version 1.8.2 please
> See the upgrade section at the end of this guide.

This guide will walk you through a production installation of Fwego using Docker 
on Ubuntu. This document aims to provide a walkthrough for servers running Ubuntu 
20.04.4 LTS. These instructions have been tested with a clean install of Ubuntu 
20.04.4 LTS and a user account with root access or the ability to run Docker containers. 

## Guide 

```bash
# Ensure your system is upto date
sudo apt update
# Docker Setup
sudo apt install docker
# Your user must be in the Docker group to run docker commands
sudo usermod -aG docker $USER
# Refresh the group so you don't need to relog to get docker permissions
newgrp docker 
# Change FWEGO_PUBLIC_URL to your domain name or http://YOUR_SERVERS_IP if you want
# to access Fwego remotely.
# This command will run Fwego with it's data stored in the new fwego_data docker 
# volume.
docker run -e FWEGO_PUBLIC_URL=http://localhost \
--name fwego \
-d \
--restart unless-stopped \
-v fwego_data:/fwego/data \
-p 80:80 \
-p 443:443 \
digitranslab/fwego:1.30.1
# Watch the logs for Fwego to come available by running:
docker logs fwego
```

## Further information 

Please refer to the [Install with Docker](install-with-docker.md) guide for how to
configure and maintain your Docker based Fwego server.

## Upgrade from Fwego 1.8.2 or earlier

The [Old Install on Ubuntu](old-install-on-ubuntu.md) guide is now deprecated. We are 
asking any users who wish to run Fwego on Ubuntu to instead install Docker and use our
official Docker images to run Fwego. This guide explains how to migrate an existing
Fwego Ubuntu install to use our official Docker images.

> If you were previously using a separate api.your_fwego_server.com domain this is no
> longer needed. Fwego will now work on a single domain accessing the api at 
> YOUR_DOMAIN.com/api. 

### Migration Steps

```bash
# === Docker Install ===
#
# Install Docker following the guide at https://docs.docker.com/engine/install/ubuntu/.
# If you have already installed Docker then please skip this section.
#
# The steps are summarized below but we encourage you to follow the guide itself:
#
sudo apt-get remove docker docker-engine docker.io containerd runc
# Setup docker
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
# Add yourself to the docker group
sudo usermod -aG docker $USER
newgrp docker

# Verify Docker install worked you should see:
#
# Unable to find image 'hello-world:latest' locally
# latest: Pulling from library/hello-world
# ...
# Hello from Docker!

docker run hello-world

# === Fwego Upgrade ===
# When you are ready to stop your old Fwego server by running
sudo supervisorctl stop all

# === Extract your secret key ===

# Extract your current SECRET_KEY value from /etc/supervisor/conf.d/fwego.conf
cat /etc/supervisor/conf.d/fwego.conf | sed -nr "s/^\s*SECRET_KEY='(\w+)',/\1/p" > .existing_secret_key

# Check this file just contains your exact secret key by comparing it with 
# /etc/supervisor/conf.d/fwego.conf 
cat .existing_secret_key

# === Configure your Postgres to allow connections from Docker ===

# 1. Find out what version of postgresql is installed by running 
sudo ls /etc/postgresql/ 
# 2. Open /etc/postgresql/YOUR_PSQL_VERSION/main/postgresql.conf for editing as root
# 3. Find the commented out # listen_addresses line.
# 4. Change it to be:
listen_addresses = '*'          # what IP address(es) to listen on;
# 5. Open /etc/postgresql/YOUR_PSQL_VERSION/main/pg_hba.conf for editing as root
# 6. Add the following line to the end which will allow docker containers to connect.
host    all             all             172.17.0.0/16           md5
# 7. Restart postgres to load in the config changes.
sudo systemctl restart postgresql
# 8. Check the logs do not have errors by running
sudo less /var/log/postgresql/postgresql-YOUR_PSQL_VERSION-main.log

# === Launch Fwego ===

# Please change this variable to the password used by the fwego user in your 
# postgresql database.
YOUR_FWEGO_DATABASE_PASSWORD=yourpassword
# Change FWEGO_PUBLIC_URL to your domain name or http://YOUR_SERVERS_IP if you want
# to access Fwego remotely.
# This command will run Fwego so it uses your existing postgresql database and your
# existing user uploaded files in /fwego/media. 
# It will store it's redis database and password, any data related to the automatic 
# HTTPS setup provided by Caddy in the new fwego_data docker volume.
docker run \
  -d \
  --name fwego \
  -e SECRET_KEY_FILE=/fwego/.existing_secret_key \
  -e FWEGO_PUBLIC_URL=http://localhost \
  --add-host host.docker.internal:host-gateway \
  -e DATABASE_HOST=host.docker.internal \
  -e DATABASE_USER=fwego \
  -e DATABASE_PASSWORD=$YOUR_FWEGO_DATABASE_PASSWORD \
  --restart unless-stopped \
  -v $PWD/.existing_secret_key:/fwego/.existing_secret_key \
  -v fwego_data:/fwego/data \
  -v /fwego/media:/fwego/data/media \
  -p 80:80 \
  -p 443:443 \
  digitranslab/fwego:1.30.1
# Check the logs and wait for Fwego to become available
docker logs fwego
```

Please refer to the [Install with Docker](install-with-docker.md) guide in the future
and for more information on how to manage your Docker based Fwego install.
