raw_data = '''CREATE TABLE tripdata;
id VARCHAR NOT NULL,
pickup_date DATETIME, 
pickup_datetime DATETIME,
dropoff_datetime DATETIME,
fare_amount FLOAT
'''

transformed_data = ''' CREATE TABLE tripdata_metrics;
month DATE,
sat_mean_trip_count FLOAT,
sat_mean_fare_trip FLOAT,
sat_mean_duration_per_trip FLOAT,
sat_mean_trip_count FLOAT,
sat_mean_fare_trip FLOAT,
sat_mean_duration_per_trip FLOAT
'''