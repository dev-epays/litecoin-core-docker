# litecoin-core-docker

docker-compose example
```
services:
  core:
    build: https://github.com/dev-epays/litecoin-core-docker.git
    environment:
      RPC_USER: "litecoin"
      RPC_PASSWORD: "litecoin"
```
