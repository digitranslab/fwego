# Debugging connection issues

On launching Fwego if you encountered the "Backend URL mis-configuration detected" 
or you are having trouble connecting to your Fwego server this tutorial will explain 
why this error can occur how to fix it. 

## Possible cause of the error

Fwego needs to know the hostname where it hosted for a number of practical and 
security reasons. It cannot safely discover this hostname automatically and instead
relies on you setting it correctly. In the docker and docker-compose installs it 
defaults to using `http://localhost`. If you then try to access Fwego from a different
machine your browser will still be configured to look for Fwego at `http://localhost`,
which does not exist on the different machine, which is the usual cause of this error.

## Fixing a Docker Install

Ensure you have set the environment variable `FWEGO_PUBLIC_URL` to the URL you are 
using the access Fwego on. The following three sections show how to do this depending
on how you are accessing your Fwego server.

### Access via a domain name

If you are accessing your Fwego server using a domain name then you should launch 
Fwego like so:
```bash
docker run \
  -e FWEGO_PUBLIC_URL=https://YOUR_DOMAIN_HERE \
  # ... followed by the rest of your normal fwego docker arguments 
```

### Access via a domain name with automatic HTTPS

If you are accessing your Fwego server using a domain name and you want the Fwego
Caddy server to automatically handle HTTPS for you then launch Fwego like so. If
you still want to be able to access your Fwego from http://localhost add
`,http://localhost` onto the FWEGO_CADDY_ADDRESSES.
```bash
docker run \
  -e FWEGO_PUBLIC_URL=https://YOUR_DOMAIN_HERE \
  -e FWEGO_CADDY_ADDRESSES=https://YOUR_DOMAIN_HERE \
  # ... followed by the rest of your normal fwego docker arguments 
```

### Accessing via an IP address

If you are accessing your Fwego server using an IP address then you should launch
Fwego like so: 
```bash
docker run \
  -e FWEGO_PUBLIC_URL=http://YOUR_IP_ADDRESS_HERE \
  # ... followed by the rest of your normal fwego docker arguments 
```

### Accessing using a non-standard port

If you have or want to access Fwego using a different port other than 80 (`-p 80:80`) 
then you also need to set the environment variable `WEB_FRONTEND_PORT`. You also need 
to ensure you properly change the `-p 80:80` argument to 
`-p YOUR_CUSTOM_PORT:80` and also update the FWEGO_PUBLIC_URL to include
the port at the end. 

> Please note that ports 3000, 5432, 1085 and
> 8000 are already bound to within the Docker container and so you should pick a different
> port for YOUR_CUSTOM_PORT. This is because the embedded Caddy reverse proxy listens
> for connections at $FWEGO_PUBLIC_URL, and so by adding a port onto this you will
> also make Caddy inside the container listen on that port. 

```bash
docker run \
  -e FWEGO_PUBLIC_URL=https://YOUR_IP_OR_DOMAIN_HERE:YOUR_CUSTOM_PORT \
  -e WEB_FRONTEND_PORT=YOUR_CUSTOM_PORT \
  -p YOUR_CUSTOM_PORT:80 \
  # ... followed by the rest of your normal fwego docker arguments 
```


## Fixing a Docker-Compose Install

Ensure you have set the environment variable `FWEGO_PUBLIC_URL` to the URL you are
using the access Fwego on. See the 
[Install with docker compose](../installation/install-with-docker-compose.md) guide
to see the various ways you can set this variable using docker compose.

The following three sections show how to do this depending on how you are accessing 
your Fwego server. Please remember to also include any additional environment 
variables and arguments that are explained in the guide above.

### Access via a domain name

If you are accessing your Fwego server using a domain name then you should launch
Fwego like so 
```bash
FWEGO_PUBLIC_URL=https://YOUR_DOMAIN_HERE docker-compose up -d
```

### Access via a domain name with automatic HTTPS

If you are accessing your Fwego server using a domain name and you want the Fwego
Caddy server to automatically handle HTTPS for you then launch Fwego like so. If
you still want to be able to access your Fwego from http://localhost add 
`,http://localhost` onto the FWEGO_CADDY_ADDRESSES.
```bash
FWEGO_PUBLIC_URL=https://YOUR_DOMAIN_HERE \
FWEGO_CADDY_ADDRESSES=https://YOUR_DOMAIN_HERE \
docker-compose up -d
```

### Accessing via an IP address

If you are accessing your Fwego server using an IP address then you should launch
Fwego like so:
```bash
FWEGO_PUBLIC_URL=https://YOUR_IP_HERE docker-compose up -d
```

### Accessing using a non-standard port

If you have or want to access Fwego using a different port other than 80 and
then you also need to set the environment variable `WEB_FRONTEND_PORT`.

```bash
FWEGO_PUBLIC_URL=https://YOUR_IP_OR_DOMAIN_HERE:YOUR_CUSTOM_PORT \
WEB_FRONTEND_PORT=YOUR_CUSTOM_PORT \
docker-compose up -d
```

## Fixing an install using standalone Fwego service images

Fwego also provides the `fwego/backend` and `fwego/web-frontend` images for users
who want to host and co-ordinate the various Fwego services themselves. Using
these images you instead need to set the following environment variables on all 
containers running these images. Please note that the `FWEGO_PUBLIC_URL` environment
variable is not used by these standalone images.

* `PUBLIC_BACKEND_URL` (default `http://localhost:8000`): The publicly accessible URL of
  the backend. Should include the port if non-standard. 
* `PRIVATE_BACKEND_URL` (default `http://backend:8000`): Not only the browser, but also
  the web-frontend server should be able to make HTTP requests to the backend. It might
  not have access to the `PUBLIC_BACKEND_URL` or there could be a more direct route,
  (e.g. from container to container instead of via the internet). In case of the
  development environment the backend container be accessed via the `backend` hostname
  and because the server is also running on port 8000 inside the container, the private
  backend URL should be `http://backend:8000`.
* `PUBLIC_WEB_FRONTEND_URL` (default `http://localhost:3000`): The publicly accessible
  URL of the web-frontend. Should include the port if non-standard.

## Further help 

Please post on the [community forum](https://fwego.io) if you are having further
troubles or are using another installation method.
