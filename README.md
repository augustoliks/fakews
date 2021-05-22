# mock-ws-server

WebServer com um canal websocket. Ideal parar testar ambientes Web.

# Execução 

Provisionar o serviço com docker-compose:

```shell
docker-compose up --build -d
```

Testar conexão:

```shell
websocat ws://127.0.0.1:8090/ws
```

> O exemplo utilizou o utilitário de linha de comando websocat, para mais detalhes desta ferramenta, acessar: https://github.com/vi/websocat
