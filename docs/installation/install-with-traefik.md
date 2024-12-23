# Installing Fwego with Traefik

If you are using [Traefik](https://doc.traefik.io/traefik/) the example below will show
you how to configure Fwego to work with Traefik.

## Example Traefik compose file

See below for an example docker-compose file that will enable Fwego with Traefik.

```
version: "3.4"
services:
  fwego:
    image: digitranslab/fwego:1.30.1
    container_name: fwego
    labels:
        # Explicitly tell Traefik to expose this container
        - "traefik.enable=true"
        # The domain the service will respond to
        - "traefik.http.routers.fwego.rule=Host(`domain.com`)"
    environment:
      - FWEGO_PUBLIC_URL=https://domain.com
    volumes:
      - fwego_data:/fwego/data
volumes:
  fwego_data:
```
