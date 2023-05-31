# litecoin-core-docker

docker-compose example
```
services:
  core:
    build: git@github.com:dev-epays/litecoin-core-docker.git#main
    environment:
      RPC_USER: "litecoin"
      RPC_PASSWORD: "litecoin"
    volumes:
      - /home/blockchain/.dogecoin:/home/dogecoin/.dogecoin
```
