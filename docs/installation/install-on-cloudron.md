# Installation on Cloudron

> Any questions, problems or suggestions with this guide? Ask a question in our
> [community](https://community.fwego.io/) or contribute the change yourself at
> https://github.com/digitranslab/fwego/-/tree/develop/docs .

Cloudron is a complete solution for running apps on your server and keeping them
up-to-date and secure. If you don't have Cloudron installed on a server you can follow
the [installation instructions here ](https://docs.cloudron.io/installation/). Ensure
you follow the installation guide to the end and log into the cloudron app store. Once
you have Cloudron installed and running on your service you can follow the steps below
to install the Fwego app.

> Basic experience with the Cloudron CLI is required.

## Install Cloudron CLI

The Cloudron CLI runs on your local machine and not the server. It can be installed on
Linux/Mac using the following command. More information about installing can be found on
their website at
[https://docs.cloudron.io/custom-apps/cli/](https://docs.cloudron.io/custom-apps/cli/).

```
$ # Do not attempt to install on your server, but instead on your local machine.
$ sudo npm install -g cloudron
```

## Installing Fwego

If you have not already been logged into your Cloudron platform you can do so by
executing the following command.

```
$ cloudron login my.{YOUR_DOMAIN}
```

When you have successfully logged in, you need to clone the latest Fwego repository to
your machine. This contains the Cloudron manifest file that you need when installing the
app.

```
$ git clone --branch master https://github.com/digitranslab/fwego.git
$ cd fwego/deploy/cloudron
```

After that you can install the Fwego Cloudron app by executing the following commands.

```
$ cloudron install -l fwego.{YOUR_DOMAIN} --image fwego/cloudron:1.30.1
App is being installed.
...
App is installed.
```

> All the available versions can be found here:
> [https://hub.docker.com/r/fwego/cloudron](https://hub.docker.com/r/fwego/cloudron)

> If you get Failed to install app: 402 message: Missing token errors make sure you
> have fully completed the installation of the cloudron server linked at the start.
> Specifically you need to login to your cloudron account on your server's cloudron
> webpage.

When the installation has finished you can visit your domain and create a new account
from there.

## Updating

When a new Fwego version becomes available you can easily update to that version.
First you need to figure out what your app id is. You can do so by executing the
`cloudron list` command. After determining your app id, if you do not have a local
copy of the Fwego repository then run the following command to get one:

```
git clone --branch master https://github.com/digitranslab/fwego.git
cd fwego/deploy/cloudron
```

If you do have an existing copy of the Fwego repo then run the following commands
from the root of the repository to update the repository to the latest version:

```
cd fwego # change to where-ever your local fwego repo is found
git pull
cd deploy/cloudron
```

Once you have an up-to date local copy of the Fwego repo, and you have changed into 
the `fwego/deploy/cloudron` folder, you can upgrade your cloudron fwego server to 
the latest version by running the following command:

```
cloudron update --app {YOUR_APP_ID} --image fwego/cloudron:1.30.1
```

> Note that you must replace the image with the most recent image of Fwego. The
> latest version can be found here:
> [https://github.com/digitranslab/fwego/container_registry/1692077](https://github.com/digitranslab/fwego/container_registry/1692077)

## Application builder domains

Fwego has an application builder that allows to deploy an application to a specific
domain. Because Cloudron has a reverse proxy that routes a domain to the right Cloudron
app, the deployed application isn't automatically available on the chosen domain.

To make this work, you must add a domain alias in the Cloudron settings. This can be
done by going to the settings of your Fwego app, then click on `Location`, click on
`Add an alias`, and then add the domain you've published the application to in  Fwego.
Make sure that the alias matches the full domain name in Fwego. After that, Cloudron
will request the SSL certificate, and then you can visit your domain.

It's also possible to add a wildcard alias to Cloudron, but the SSL certificate then
doesn't work out of the box. Some additional settings on Cloudron might be required to
make it work.
