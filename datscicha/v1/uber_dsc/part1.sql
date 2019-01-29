-- For each of the cities 'Qarth' and 'Meereen', calculate 90th percentile difference between Actual and Predicted ETA for all completed trips within the last 30 day

select percentile_cont(0.9) within group (order by t.actual_eta - t.predicted_eta) as ninetiethPercentileDiff
from trips as t
left join cities as c on t.city_id = c.city_id
where c.city_name in ('Qarth','Meereen') and t.status = "completed" and t.request_at > (current_date - interval '30 days');

-- A signup is defined as an event labeled ‘sign_up_success’ within the events table. For each city (‘Qarth’ and ‘Meereen’) and each day of the week, determine the percentage of signups in the first week of 2016 that resulted in completed a trip within 168 hours of the sign up date.

select q1.city_name,q1.day_of_week,sum(q2.num_riders)*100/sum(q1.num_riders) as percentage_of_drivers
from (
    select c.city_name as city_name,extract(dow from e._ts) day_of_week,count(distinct e.rider_id) num_riders
    from events e 
    left join cities c on e.city_id=c.city_id
    where e.event_name='sign_up_success' and c.city_name in ('Quarth','Meeren') and extract(week from e._ts) = 1 and extract(year from e._ts) = 2016
    group by c.city_name,extract(dow from e._ts)
) q1
left join (
    select c.city_name as city_name,extract(dow from e._ts) day_of_week,count(distinct e.rider_id) num_riders
    from events e
    left join cities c on e.city_id=c.city_id
    left join trips t on e.rider_id=t.driver_id
    where e.event_name='sign_up_success' and c.city_name in ('Quarth','Meeren') and extract(week from e._ts) = 1 and extract(year from e._ts) = 2016 and t.status='completed' and date_part('day',t.request_at-e._ts)*24+date_part('hour',t.request_at-e._ts)<168
    group by c.city_name,extract(dow from e._ts)
) q2 on q1.city_name=q2.city_name and q1.day_of_week=q2.day_of_week
group by q1.city_name,q1.day_of_week