# Module-1-Homework-Docker-SQL
Contains codes for solving the Module 1 Homework: Docker &amp; SQL

# Question 1. Understanding docker first run

### This is Docker File !
```bash
FROM python:3.12.8

RUN pip install pandas

ENTRYPOINT [ "bash" ]
```

### ------- Docker Command To test the PIP Version -------

- I run 
```bash
docker build -t test1:pandas .
```
- Then I run
```bash
docker run -it test:pandas
```
- I tried pip --version then I got the value of **24.3.1** in python **3.12.8**

------------------------------------------------------------------------------------------------------

# Question 2: Understanding Docker Networking and Docker-Compose

Given the following `docker-compose.yaml`:

```yaml
services:
  db:
    container_name: postgres
    image: postgres:17-alpine
    environment:
      POSTGRES_USER: 'postgres'
      POSTGRES_PASSWORD: 'postgres'
      POSTGRES_DB: 'ny_taxi'
    ports:
      - '5433:5432'
    volumes:
      - vol-pgdata:/var/lib/postgresql/data

  pgadmin:
    container_name: pgadmin
    image: dpage/pgadmin4:latest
    environment:
      PGADMIN_DEFAULT_EMAIL: "pgadmin@pgadmin.com"
      PGADMIN_DEFAULT_PASSWORD: "pgadmin"
    ports:
      - "8080:80"
    volumes:
      - vol-pgadmin_data:/var/lib/pgadmin  

volumes:
  vol-pgdata:
    name: vol-pgdata
  vol-pgadmin_data:
    name: vol-pgadmin_data
```

## Answer:
The hostname and port that pgadmin should use to connect to the Postgres database are:
```bash
db:5432
```
