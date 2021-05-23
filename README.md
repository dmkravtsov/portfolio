# Portfolios
Steps to create database for portfolios:

1. Create docker volume: docker volume create --name vol_1    (one_time)
2. Create and run dockerfile: docker run --rm --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5400:5432 -v vol_1:/var/lib/postgresql/data postgres:latest

3. Run db.py 
4. Run create_tables.py
5. Visit and login to: http://localhost/pgadmin4/browser/
6. Create new server connection: 

Host name: 0.0.0.0
Port: 5400
Database: postgres
Username: postgres
Password: docker