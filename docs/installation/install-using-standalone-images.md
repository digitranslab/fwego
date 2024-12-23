# Install using Standalone Images

> Any questions, problems or suggestions with this guide? Ask a question in our
> [community](https://community.fwego.io/) or contribute the change yourself at
> https://github.com/digitranslab/fwego/-/tree/develop/docs .

> Docker version 19.03 is the minimum required to build Fwego. It is strongly
> advised however that you install the latest version of Docker available.
> Please check that your docker is up to date by running `docker -v`.

Fwego consists of a number of services, two of which are built and provided as 
separate standalone images by us:
* `fwego/backend:1.30.1` which by default starts the Gunicorn Django backend server 
  for Fwego but is also used to start the celery workers and celery beat services.
* `fwego/web-frontend:1.30.1` which is a Nuxt server providing Server Side rendering 
  for the website.

If you want to use your own container orchestration software like Kubernetes then these
images let you run and scale these different parts of Fwego independently. 

For an example of how to use these images see the
[`docker-compose.yml`](https://github.com/digitranslab/fwego/-/blob/master/docker-compose.yml) 
in the root of our repository. 

## All Services needed to run Fwego

These are all the services you need to set up to run a Fwego using the standalone 
images:

* `fwego/backend:1.30.1` (default command is `gunicorn`)
* `fwego/backend:1.30.1` with command `celery-worker`
* `fwego/backend:1.30.1` with command `celery-export-worker`
* `fwego/web-frontend:1.30.1` (default command is `nuxt-local`)
* A postgres database 
* A redis server

## Configuration Caveats

* See [Configuring Fwego](configuration.md) for specific details on the supported 
  environment variables.
* You must set `FWEGO_PUBLIC_URL` (usually only when behind your a reverse proxy, see 
  below for details) or `PUBLIC_BACKEND_URL` and `PUBLIC_WEB_FRONTEND_URL`
* You must set `PRIVATE_BACKEND_URL` so the web-frontend server can make direct 
  HTTP requests to the backend. The web-frontend might not have access to the 
  `PUBLIC_BACKEND_URL` or `FWEGO_PUBLIC_URL`, or there could be a more direct internal
  route it could use. (e.g. from container to container instead of via the internet). 
* These images do not come with a Caddy Reverse proxy and so the 
  `FWEGO_CADDY_ADDRESSES` environment variable used in other installation methods 
  has no affect.
* You must set a `SECRET_KEY` environment variable for the backend gunicorn server.
* See our example [`Caddyfile`](https://github.com/digitranslab/fwego/-/blob/master/Caddyfile)
  for an example on how to setup a reverse proxy correctly with Fwego. In summary you
  need to:
  * Redirect `/api/` and `/ws/` requests to the backend gunicorn service without 
    dropping these prefixes.
  * Serve the files in the `/fwego/media` folder in the backend gunicorn service 
    (share with your proxy using a volume) at the `/media` endpoint. Ensure 
    that requests with a `dl` query parameter have a `Content-disposition` header added
    with the value of `attachment; filename=THE_DL_QUERY_PARAM_VALUE` 
  * Send all other requests to the web-frontend service.
* You must provide all email related environment variables to both the backend and 
  celery-worker services. This is because the `celery-worker` service is the one 
  actually connecting via SMTP to send emails.
