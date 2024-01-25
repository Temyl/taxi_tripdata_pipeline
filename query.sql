select toStartOfMonth(pickup_date) as month,
       ROUND(AVG(DAYOFWEEK(pickup_date) = 7), 1) as sat_mean_trip_count,
       ROUND(AvG(IF(DAYOFWEEK(pickup_date) = 7, fare_amount, 0)), 1) as sat_mean_fare_trip,
       ROUND(AVG(IF(DAYOFWEEK(pickup_date)= 7, toUInt32(TIMEDIFF(dropoff_datetime, pickup_datetime))/60, 0)), 1) AS sat_mean_duration_per_trip,
       ROUND(AVG(DAYOFWEEK(pickup_date) = 1), 2) as sun_mean_trip_count,
       ROUND(AvG(IF(DAYOFWEEK(pickup_date) = 1, fare_amount, 0)), 2) as sun_mean_fare_trip,
       ROUND(AVG(IF(DAYOFWEEK(pickup_date)= 1, toUInt32(TIMEDIFF(dropoff_datetime, pickup_datetime))/60, 0)), 1) AS sun_mean_duration_per_trip
from tripdata
where pickup_date between '2014-1-1' and '2016-12-31'
group by month
order by month; 