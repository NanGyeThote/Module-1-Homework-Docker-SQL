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
- I tried pip --version then I got my answer.

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
as shown in my answer
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
as shown in my answer
```

I run with this because when i tried copying from Jupyter Notebook to ny_taxi database, the data had type error and not all rows had been inserted.

------------------------------------------------------------------------------------------------------

# Question 5. Three biggest pickup zones

```bash
# Load taxi zone lookup file to map LocationID to zone names
zones = pd.read_csv('taxi_zone_lookup.csv')

# Initialize a dictionary to track total amount per pickup location
pickup_totals = {}

# Read the dataset in chunks
df_iter = pd.read_csv(
    'green_tripdata_2019-10.csv',
    iterator=True,
    chunksize=100000,
    dtype={'total_amount': float, 'PULocationID': int},
    parse_dates=['lpep_pickup_datetime'],
    low_memory=False
)

# Process each chunk
for df in df_iter:
    # Filter data for 2019-10-18
    df_filtered = df[df['lpep_pickup_datetime'].dt.date == pd.to_datetime('2019-10-18').date()]
    
    # Sum total_amount per pickup location
    pickup_sums = df_filtered.groupby('PULocationID')['total_amount'].sum()
    
    # Accumulate total amounts across chunks
    for loc_id, total in pickup_sums.items():
        if total > 13000:
            pickup_totals[loc_id] = pickup_totals.get(loc_id, 0) + total

# Sort pickup locations by total_amount
top_pickups = sorted(pickup_totals.items(), key=lambda x: x[1], reverse=True)

# Check how many locations meet the criteria
print(f"Total locations with total_amount > 13000: {len(top_pickups)}")

# Get the top 3 locations if available
top_pickup_names = [zones.loc[zones['LocationID'] == pid, 'Zone'].values[0] for pid, _ in top_pickups[:3]]

# Print the result
print(f"The top pickup locations with total_amount > 13,000 on 2019-10-18 were: {', '.join(top_pickup_names)}")
```

## Answers:
```bash
as shown in my answer
```

I run with this because when i tried copying from Jupyter Notebook to ny_taxi database, the data had type error and not all rows had been inserted.

------------------------------------------------------------------------------------------------------

# Question 6. Largest tip

```bash
# Load your dataset
df = pd.read_csv('green_tripdata_2019-10.csv', dtype={'column_name': str}, low_memory=False)

# Convert 'lpep_pickup_datetime' and 'lpep_dropoff_datetime' to datetime if not already
df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])
df['lpep_dropoff_datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'])

# Filter for pickups in "East Harlem North" and within October 2019
east_harlem_north = df[(df['PULocationID'] == 74) & 
                       (df['lpep_pickup_datetime'].dt.month == 10) & 
                       (df['lpep_pickup_datetime'].dt.year == 2019)]

# Group by dropoff location and get the dropoff zone with the largest tip
dropoff_zone_with_largest_tip = east_harlem_north.groupby('DOLocationID')['tip_amount'].max().idxmax()

# Find the drop-off zone corresponding to that DOLocationID
# Assuming 'taxi_zone_lookup.csv' contains the mapping between LocationID and Zone
zone_lookup = pd.read_csv('taxi_zone_lookup.csv')

# Find the zone name
largest_tip_zone = zone_lookup[zone_lookup['LocationID'] == dropoff_zone_with_largest_tip]['Zone'].values[0]

print(f"The drop-off zone with the largest tip is: {largest_tip_zone}")
```

## Answers:
```bash
as shown in my answer
```

I run with this because when i tried copying from Jupyter Notebook to ny_taxi database, the data had type error and not all rows had been inserted.

------------------------------------------------------------------------------------------------------

# Question 7. Terraform Workflow

I have some pre-knowledge about Terraform!

## Answers:
```bash
as shown in my answer
```

------------------------------------------------------------------------------------------------------


