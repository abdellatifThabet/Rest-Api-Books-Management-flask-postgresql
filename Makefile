build:
	@docker-compose build

db-upgrade:
	@docker-compose up -d db
	@sleep 5
	@docker-compose run python-api flask db upgrade --directory python-api/migrations

stop:
	@docker-compose down --remove-orphans

db-migrate: 
	@docker-compose run python-api flask db migrate --directory python-api/migrations

run: stop build db-upgrade
	@docker-compose up  --remove-orphans

