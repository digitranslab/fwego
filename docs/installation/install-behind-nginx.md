# Installing Fwego behind Nginx

If you have an [Nginx server](https://www.nginx.com/) this guide will explain how to
configure it to pass requests through to Fwego.

We strongly recommend you use our `digitranslab/fwego:1.30.1` image or the example
`docker-compose.yml` files (excluding the `.no-caddy.yml` variant) provided in
our [git repository](https://github.com/digitranslab/fwego/-/tree/master/deploy/nginx/).

These come with a pre-configured, simple and lightweight Caddy http server which 
simplifies your life by:

1. Routing requests to the correct internal Fwego services
2. Enabling websocket connections for realtime collaboration
3. Serving user uploaded files
4. **And it still runs behind your own reverse proxy with no problems**

> If you do not want to use our embedded Caddy service behind your Nginx then
> make sure you are using one of the two following deployment methods: 
>
> * Your own container setup with our single service `fwego/backend:1.30.1`
    and `fwego/web-frontend:1.30.1` images.
> * Or our `docker-compose.no-caddy.yml` example file in our [git repository](https://github.com/digitranslab/fwego/-/tree/master/deploy/nginx/).
> 
> Then you should use **Option 2: Without our embedded Caddy** section instead.

## Option 1: With our embedded Caddy

> You can find a Dockerized working example of using Nginx with Fwego in our git repo in
> the [deploy/nginx/recommended](https://github.com/digitranslab/fwego/-/tree/master/deploy/nginx/)
> folder.

Follow this option if you are using:

* The all-in-one Fwego image `digitranslab/fwego:1.30.1`
* Any of the example compose files found in the root of our git
  repository `docker-compose.yml`/`docker-compose.local-build.yml`
  /`docker-compose.all-in-one.yml`

### Prerequisites

We assume you already have a Nginx server running which you know how to configure.

Additionally, we assume you are using a debian based operating system and have already
successfully deployed Fwego. 

### Step 1 - Configure Fwego's FWEGO_PUBLIC_URL

Fwego needs to know the URL it will be accessed on. We'll assume you will be hosting
Fwego on a subdomain and so you should set the following environment variable on your
Fwego deployment (see [Configuring Fwego](./configuration.md) for more details).

```
FWEGO_PUBLIC_URL=http://fwego.example.com
```

### Step 2 - Add nginx config for Fwego

Create a new `fwego.conf` in `/etc/nginx/sites-available/` with the following contents:

> Make sure to replace any http://localhost:PORT references with the correct ones for
> your particular Fwego deployment.

```
server {
    server_name fwego.example.com;

    # Upgrade websocket requests and route the api backend
    location ~ ^/(api|ws)/ {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_pass http://localhost:8080;
    }

    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $http_host;
        proxy_http_version 1.1;
        proxy_pass http://localhost:8080;
    }
}
```

### Step 3 - Enable the new Fwego site

Finally, you should enable your new Fwego site and restart your Fwego server if you
made environment variable changes.

```bash
 sudo ln -s /etc/nginx/sites-available/fwego.conf /etc/nginx/sites-enabled/fwego.conf
 sudo systemctl reload nginx
```

You should now be able to access Fwego on you configured subdomain.

## Option 2: Without our embedded Caddy

> You can find a Dockerized working example of using Nginx with Fwego in our git repo in
> the [deploy/nginx/no-caddy](https://github.com/digitranslab/fwego/-/tree/master/deploy/nginx/)
> folder.

Follow this option if you are using:

* Our standalone `fwego/backend:1.30.1` and `fwego/web-frontend:1.30.1` images with
  your own container orchestrator.
* Or the `docker-compose.no-caddy.yml` example docker compose file in the root of our
  git repository.

### Prerequisites

We assume you already have a Nginx server running which you know how to configure.

Additionally, we assume you are using a debian based operating system and have already
successfully deployed Fwego. If you are using a different setup the 
general steps and Nginx config should still be a useful starting point for you,
but you might have to run different commands.

### Step 1 - Mount the media volume so Nginx can serve uploaded files

You need to ensure user uploaded files are accessible in a folder for Nginx to serve. In
the rest of the guide we will use the example `/var/web` folder for this purpose.

If you are using the `fwego/backend:1.30.1` image then you can do this by adding
`-v /var/web:/fwego/data/media` to your normal `docker run` command used to launch the
Fwego backend.

If you are instead using the `docker-compose.no-caddy.yml` then you can change all of
the
`- media:/fwego/media` mounts to be `- /var/web:/fwego/media`.

### Step 2 - Configure Fwego's FWEGO_PUBLIC_URL

Fwego needs to know the URL it will be accessed on. We'll assume you will be hosting
Fwego on a subdomain and so you should set the following environment variable on your
Fwego deployment (see [Configuring Fwego](./configuration.md) for more details).

```
FWEGO_PUBLIC_URL=http://fwego.example.com
```

### Step 3 - Add nginx config for Fwego

Create a new `fwego.conf` in `/etc/nginx/sites-enabled/` with the following contents:

> Make sure to replace any http://localhost:PORT references with the correct ones for
> your particular Fwego deployment.

```
server {
    server_name fwego.example.com;

    # Upgrade websocket requests and route the api backend
    location ~ ^/(api|ws)/ {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_pass http://localhost:8000;
    }

    location /media/ {
        if ($arg_dl) {
            add_header Content-disposition "attachment; filename=$arg_dl";
        }
        # TODO Change to your media folder location!
        alias /var/www/;
    }

    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $http_host;
        proxy_http_version 1.1;
        proxy_pass http://localhost:3000;
    }
}
```

### Step 4 - Enable the new Fwego site

Finally, you should enable your new Fwego site and restart your Fwego server if you
made environment variable changes.

```bash
 sudo ln -s /etc/nginx/sites-available/fwego.conf /etc/nginx/sites-enabled/fwego.conf
 sudo systemctl reload nginx
```

You should now be able to access Fwego on you configured subdomain.

### Troubleshooting

If you can upload images to Fwego but no thumbnails show, or you can't re-download
them (you are getting 403 denied errors when accessing the files) then:

* Make sure the permissions on the sub-folders in /var/web are set to be readable by
  your Nginx user by running `cd /var/web && chmod 755 *`.
* Fix any file permissions found inside the `/var/web` sub-folders to be readable by
  your Nginx user.

