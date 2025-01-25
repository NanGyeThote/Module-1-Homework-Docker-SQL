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
The **hostname** and **port** that **pgadmin** should use to connect to the Postgres database are:
```bash
db:5432
```

------------------------------------------------------------------------------------------------------

# Question 3. Trip Segmentation Count

```bash
# Initialize counters
counts = {
    'up_to_1_mile': 0,
    'between_1_and_3_miles': 0,
    'between_3_and_7_miles': 0,
    'between_7_and_10_miles': 0,
    'over_10_miles': 0
}

df_iter = pd.read_csv(
    'green_tripdata_2019-10.csv',
    iterator=True,
    chunksize=100000,
    dtype={'trip_distance': float},
    parse_dates=['lpep_pickup_datetime', 'lpep_dropoff_datetime'],
    low_memory=False
)

# Process each chunk
for df in df_iter:
    counts['up_to_1_mile'] += (df['trip_distance'] <= 1).sum()
    counts['between_1_and_3_miles'] += ((df['trip_distance'] > 1) & (df['trip_distance'] <= 3)).sum()
    counts['between_3_and_7_miles'] += ((df['trip_distance'] > 3) & (df['trip_distance'] <= 7)).sum()
    counts['between_7_and_10_miles'] += ((df['trip_distance'] > 7) & (df['trip_distance'] <= 10)).sum()
    counts['over_10_miles'] += (df['trip_distance'] > 10).sum()

# Print final counts
print(counts)
```

## Answers:
```bash
104,838; 199,013; 109,645; 27,688; 35,202
```

I run with this because when i tried copying from Jupyter Notebook to ny_taxi database, the data had type error and not all rows had been inserted.
