[![augustoliks/fakews](https://img.shields.io/badge/docker--hub-augustoliks/fakews:latest-blue.svg)](https://hub.docker.com/r/augustoliks/fakews)
[![Docker Pulls](https://img.shields.io/docker/pulls/augustoliks/fakews.svg)](https://hub.docker.com/r/augustoliks/fakews/)

# fakews

Container tool that generate events in JSON format through web socket channel. The purpose of this image is help infra debug process.

# How To Run

The container was published in Docker Hub in [augustoliks/fakews](https://hub.docker.com/r/augustoliks/fakews) repository. The application generate web socket events through `8090/TCP` port.

To run container application, execute a command bellow:

```bash
$ docker run -it -p 8090:8090 augustoliks/fakews
```

Test web socket connection:

```shell
$ websocat ws://127.0.0.1:8090/ws
```

> The example used `websocat` CLI tool to get mock events. Read this link to see more details about this tool: https://github.com/vi/websocat

# How To Run Locally With NGINX Proxy

Prosioning `fakews` back in NINGX proxy:

```shell
docker-compose up --build -d
```

Test connections through NGINX proxy:

```shell
websocat ws://127.0.0.1:8080/ws
```
