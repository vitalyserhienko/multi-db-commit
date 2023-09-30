run:
	docker run --rm -d --name postgres-db-1 -p 5432:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=db postgres --max_prepared_transactions=100
	docker run --rm -d --name postgres-db-2 -p 5433:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=db postgres --max_prepared_transactions=100
	docker ps

stop:
	docker stop postgres-db-1
	docker stop postgres-db-2
	docker ps -a

clean:
	make stop
	make run
