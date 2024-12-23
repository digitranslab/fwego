# Deprecated Guide - Installation on Ubuntu

> Warning: This guide has been deprecated as of version 1.9 of Fwego. Please follow
> the [Install on Ubuntu - Upgrade from 1.8.2 Section](install-on-ubuntu.md) 
> if you installed Fwego 1.8.2 using this guide to upgrade.

This deprecated and now unsupported guide will walk you through a production
installation of Fwego. Specifically this document aims to provide a walkthrough for
servers running Ubuntu 18.04.03 LTS. These instructions have been tested with a clean
install of Ubuntu 18.04.03 LTS and a user account with root access. Note that without
root access, many of the instructions cannot be executed, so root access is necessary in
almost all cases.

# Prerequisites

## Update & Upgrade Packages

In order to make sure that we're getting the correct and new versions of any packages we
install, we need to update and upgrade our packages.

```bash
$ sudo apt update
$ sudo apt upgrade -y
```

## A quick note on firewalls

In order to serve web content you will need to open up the HTTP (and HTTPS) ports 80
(and 443). You can do this with a firewall - `ufw` might be good place to start if you
are new to firewalls.

# Installation

## Install & Setup PostgreSQL

Fwego uses PostgreSQL in order to store its user data. You can install PostgreSQL with
the following commands:

```bash
$ sudo apt install postgresql postgresql-contrib -y
# Make sure you replace 'yourpassword' below with a secure password for your database
# user.
$ sudo -u postgres psql << EOF
create database fwego;
create user fwego with encrypted password 'yourpassword';
grant all privileges on database fwego to fwego;
EOF
```

Make sure that you use a secure password instead of `yourpassword`! Also take care that
you use the password you've chosen in any upcoming commands that need the PostgreSQL
fwego user password.

## Install & Setup Redis

Fwego uses Redis for asynchronous tasks and the real time collaboration. You can
install Redis with the following commands.

```bash
$ sudo add-apt-repository ppa:chris-lea/redis-server
$ sudo apt update
$ sudo apt install redis-server -y
$ sudo sed -i 's/supervised no/supervised systemd/g' /etc/redis/redis.conf
$ sudo systemctl enable --now redis-server
$ sudo systemctl restart redis.service
```

Redis is not publicly accessible by default, so there is no need to setup a password.

## Install other utils

Git is required to download the source code of Fwego so you can install it in the
following section. Curl will be required later in the guide to install nodejs. Install
them both using the following command:

```bash
$ sudo apt install git curl -y 
```

## Install Fwego

In this section, we will install Fwego itself. We will need a new user called
`fwego`. Fwego uses the `/fwego` directory for storing the application itself.

```bash
# Create fwego user
$ sudo useradd fwego
$ sudo passwd fwego
# Enter new UNIX password: yourpassword
# Retype new UNIX password: yourpassword

# Change to root user
$ sudo -i

# Clone the fwego project
$ mkdir /fwego
$ cd /fwego
$ git clone --branch master https://github.com/digitranslab/fwego.git
```

The password used for the `fwego` user does not have to be the same as the one used
with PostgreSQL. Just make sure that you use a secure password and that you remember it
for when you need it later.

## Install dependencies for & setup Fwego

In order to use the Fwego application, we will need to create a media directory for
the uploaded user files, a virtual environment and install some more dependencies like:
NodeJS, Yarn, Python 3.7.

First, if you are on Ubuntu version 20.04 or later you will need add the following
repository to then be able to install Python 3.7:

```bash
add-apt-repository ppa:deadsnakes/ppa
apt-get update
```

Next follow these steps:

```bash
# Create uploaded user files and media directory
$ mkdir media
$ chmod 0755 media

# Install python3.7, pip & virtualenv
$ apt install python3.7 python3.7-dev python3-pip virtualenv libpq-dev libmysqlclient-dev -y

# Create virtual environment
$ virtualenv -p python3.7 env

# Activate the virtual environment
$ source env/bin/activate

# Install backend dependencies through pip
$ pip3 install -e ./fwego/backend
# Install the premium plugin
$ pip3 install -e ./fwego/premium/backend

# Deactivate the virtual environment
$ deactivate

# Install NodeJS
$ curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
$ apt install nodejs -y

# Install yarn
$ curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
$ echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
$ apt update
$ apt install yarn -y

# Install frontend dependencies through yarn
$ cd fwego/web-frontend
$ yarn install

# Build frontend
$ ./node_modules/nuxt/bin/nuxt.js build --config-file config/nuxt.config.local.js
```

## Install NGINX

Fwego uses NGINX as a reverse proxy for its frontend and backend. Through that, you
can easily add SSL Certificates and add more applications to your server if you want to.

```bash
# Go back to fwego root directory
$ cd /fwego

# Install & Start NGINX
$ apt install nginx -y
$ service nginx start
```

## Setup NGINX

If you're unfamiliar with NGINX: NGINX uses so called "virtualhosts" to direct web
traffic from outside your network to the correct application on your server. These
virtual hosts are defined in `.conf` files which are put into the
`/etc/nginx/sites-enabled/` directory where NGINX will then process them on startup.
Fwego comes with two configuration files for NGINX. After moving these over, change
the `server_name` value in both of the files. The server name is the domain under which
you want Fwego to be reachable.

Make sure that in the following commands you replace `api.domain.com` with your own
backend domain, that you replace `fwego.domain.com` with your frontend domain and
replace `media.fwego.com` with your domain to serve the user files.

```bash
# Move virtualhost files to /etc/nginx/sites-enabled/
$ cp fwego/docs/guides/installation/configuration-files/nginx.conf /etc/nginx/sites-enabled/fwego.conf

$ rm /etc/nginx/sites-enabled/default

# Change the server_name values
$ sed -i 's/\*YOUR_BACKEND_DOMAIN\*/api.domain.com/g' /etc/nginx/sites-enabled/fwego.conf
$ sed -i 's/\*YOUR_WEB_FRONTEND_DOMAIN\*/fwego.domain.com/g' /etc/nginx/sites-enabled/fwego.conf
$ sed -i 's/\*YOUR_MEDIA_DOMAIN\*/media.domain.com/g' /etc/nginx/sites-enabled/fwego.conf

# Then restart nginx so that it processes the configuration files
$ service nginx restart
```

## Import relations into database

In the "*Install & Setup PostgreSQL*" Section, we created a database called `fwego`
for the application. Since we didn't do anything with that database it is still empty,
which will result in a non-working application since Fwego expects certain tables and
relations to exist in that database. You can create these with the following commands:

```bash
# Prepare for creating the database schema
$ source env/bin/activate
$ export DJANGO_SETTINGS_MODULE='fwego.config.settings.base'
$ export DATABASE_PASSWORD='yourpassword'
$ export DATABASE_HOST='localhost'

# Create database schema
$ fwego migrate

# Sync the template files with the database
$ fwego sync_templates

$ deactivate
```

## Install & Configure Supervisor

Supervisor is an application that starts and keeps track of processes and will restart
them if the process finishes. For Fwego this is used to reduce downtime and in order
to restart the application in the unlikely event of an unforeseen termination. You can
install and configure it with these commands:

```bash
# Install supervisor
$ apt install supervisor -y

# Create folder for fwego logs
$ mkdir /var/log/fwego/

# Move configuration files
$ cd /fwego
$ cp fwego/docs/guides/installation/configuration-files/supervisor.conf /etc/supervisor/conf.d/fwego.conf
```

You will need to edit the `fwego.conf` file (located now at
`/etc/supervisor/conf.d/`) in order to set the necessary environment variables. You will
need to change at least the following variables which can be found in the `environment=`
section. Ensure these URL variables start with http:// or https:// .

- `PUBLIC_WEB_FRONTEND_URL`: The URL under which your frontend can be reached from the
  internet.
- `PUBLIC_BACKEND_URL`: The URL under which your backend can be reached from the
  internet.
- `MEDIA_URL`: The URL under which your media files can be reached from the internet.

You can make the modifications using sed like so:

```bash
$ sed -i 's/\*YOUR_BACKEND_DOMAIN\*/https:\/\/api.domain.com/g' /etc/supervisor/conf.d/fwego.conf 
$ sed -i 's/\*YOUR_WEB_FRONTEND_DOMAIN\*/https:\/\/fwego.domain.com/g' /etc/supervisor/conf.d/fwego.conf 
$ sed -i 's/\*YOUR_MEDIA_DOMAIN\*/https:\/\/media.domain.com/g' /etc/supervisor/conf.d/fwego.conf 
```

**Backend**

- `SECRET_KEY`: The secret key that is used to generate tokens and other random strings.
  You can generate one with the following commands:
  ```bash
  $ cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 80 | head -n 1
  ```
- `DATABASE_PASSWORD`: The password of the `fwego` database user
- `DATABASE_HOST`: The host computer that runs the database (usually `localhost`)
- `REDIS_HOST`: The host computer that runs the caching server (usually `localhost`)

**Email SMTP configuration**

If you want to configure Fwego to send emails you will have to add the following
environment variables to the `/etc/supervisor/conf.d/fwego.conf` environment block.
Otherwise, by default Fwego will not send emails and instead just log them in
`/var/log/fwego/worker.error`.

* `EMAIL_SMTP` (default ``): Providing anything other than an empty string will enable
  SMTP email.
* `EMAIL_SMTP_HOST` (default `localhost`): The hostname of the SMTP server.
* `EMAIL_SMTP_USE_TLS` (default ``): Providing anything other than an empty string will
  enable connecting to the SMTP server via TLS.
* `EMAIL_SMTP_PORT` (default `25`): The port of the SMTP server.
* `EMAIL_SMTP_USER` (default ``): The username for the SMTP server.
* `EMAIL_SMTP_PASSWORD` (default ``): The password of the SMTP server.
* `FROM_EMAIL` (default `no-reply@localhost`): The 'from' email address of the emails
  that the platform sends. Like when a user requests a password recovery.

After modifying these files you need to make supervisor reread the files and apply the
changes.

```bash
# Stop NGINX service so that supervisor can take over
$ service nginx stop

# Read the newly added files
$ supervisorctl reread

# Apply the read changes
$ supervisorctl update

# Check if the startup worked correctly
$ supervisorctl status
```

If the `reread` or the `update` commands fail, try checking the logs at
`/var/log/fwego/` - it is possible that another process is listening to one of the
ports which would terminate NGINX, or parts of Fwego.

## HTTPS / SSL Support

Since you're probably serving private data with Fwego, we strongly encourage to use a
SSL certificate to encrypt the traffic between the browser and your server. You can do
that with the following commands. We will do that with certbot, which retrieves a SSL
certificate from the LetsEncrypt Certificate Authority.

If you're not installing Fwego on a completely new server, you might need to remove
previously installed `certbot` binaries from your machine. Consult the
[certbot installation instructions](https://certbot.eff.org/lets-encrypt/ubuntubionic-nginx)
for more information.

```bash
# Install certbot
$ sudo snap install core; sudo snap refresh core
$ sudo snap install --classic certbot

# Make certbot command available
$ sudo ln -s /snap/bin/certbot /usr/bin/certbot

# Start the certificate retrieval process
$ sudo certbot --nginx

# Restart nginx so that it reads the configuration created by certbot
$ supervisorctl restart nginx
```

## Conclusion

You now have a full installation of Fwego, which will keep the Front- & Backend
running even if there is an unforeseen termination of them.

## Updating existing installation to the latest version

If you already have Fwego installed on your server and you want to update to the
latest version then you can execute the following commands. This only works if there
aren't any additional instructions in the previous release blog posts.

Follow these steps if you installed after June first 2021:

```bash
$ cd /digitranslab/fwego
$ git pull
$ cd /fwego
$ source env/bin/activate
$ pip3 install -e ./fwego/backend
$ pip3 install -e ./fwego/premium/backend
$ export DJANGO_SETTINGS_MODULE='fwego.config.settings.base'
$ export DATABASE_PASSWORD='yourpassword'
$ export DATABASE_HOST='localhost'
$ fwego migrate
$ fwego sync_templates
$ deactivate
$ cd fwego/web-frontend
$ yarn install
$ ./node_modules/nuxt/bin/nuxt.js build --config-file config/nuxt.config.local.js
$ supervisorctl reread
$ supervisorctl update
$ supervisorctl restart all
```

Follow these steps if you installed before June first 2021.

```bash
$ cd /fwego
$ git pull
$ source backend/env/bin/activate
$ pip3 install -e ./backend
$ pip3 install -e ./premium/backend
$ export DJANGO_SETTINGS_MODULE='fwego.config.settings.base'
$ export DATABASE_PASSWORD='yourpassword'
$ export DATABASE_HOST='localhost'
$ fwego migrate
$ fwego sync_templates
$ deactivate
$ cd web-frontend
$ yarn install
$ ./node_modules/nuxt/bin/nuxt.js build --config-file config/nuxt.config.local.js
$ supervisorctl reread
$ supervisorctl update
$ supervisorctl restart all
```
