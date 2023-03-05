APPLICATION_NAME = register_api
DOCKER_COMPOSE = docker-compose
DOCKER_COMPOSE_EXEC = $(DOCKER_COMPOSE) exec register_api

docker-start:
	@$(DOCKER_COMPOSE) up --force-recreate --build --remove-orphans

unit-test:
	@${DOCKER_COMPOSE_EXEC} /bin/bash -c "export ENV=TEST ; pytest -s --asyncio-mode=strict"
