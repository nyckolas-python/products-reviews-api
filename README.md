# products-reviews-api
with Flask, Postgres, Docker, pep 8

# How to run a project on your local machine?
1. Install Docker https://docs.docker.com/engine/install/
1.1. Please check and specify docker-compose.yml environment variables.
2. Run `docker-compose up --build pgadmin`
3. If you have [Errno 13] Permission denied: '/var/lib/pgadmin/sessions'
use command to give permissions run:
`sudo chmod -R 777 ./pgadmin`
4. If you need pgAdmin Open http://localhost:5050/browser/ add connect to server with:
`DB_HOST: postgres`
`POSTGRES_DB: todo_api_dev`
`POSTGRES_USER: todo_api_dev`
`POSTGRES_PASSWORD: pass`
5. Run `docker-compose up --build`
6. If you have error /data/db: permission denied failed to solve run:
`sudo chmod -R 777 ./data/db`
7. Run migrations by `docker exec -it flask_api_web flask db upgrade`
8. Run to load dataset to DB `docker exec -it flask_api_web python csv_db_inserts_one.py`
If an error occurs, repeat the command.
9. Open http://localhost:5050/browser/ in browser pgAdmin
10. Open http://localhost:5000/api/v1/product/1 in browser to view product and his reviews.
11. Open http://localhost:5000/api/v1/product/1?page=1 in browser to paginate thrue reviews.
12. You can use PUT with JSON to create new review. Example:

`{
	"review": "Some new review",
	"product_id": 1,
	"title": "Some new title"
}`