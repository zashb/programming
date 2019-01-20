-- Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.
select distinct(city)
from station
where city like "%a" or city like "%e" or city like "%i" or city like "%o" or city like "%u"

-- Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.
select distinct(city)
from station
where (city like "%a" or city like "%e" or city like "%i" or city like "%o" or city like "%u") and (city like "a%" or city like "e%" or city like "i%" or city like "o%" or city like "u%")

-- Query the Name of any student in STUDENTS who scored higher than 75 Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.
select name
from students
where marks>75
order by substr(name,-3),id

-- classify triangles
select case when a+b<=c or b+c<=a or c+a<=b then "Not A Triangle" when a=b and b=c and c=a then "Equilateral" when a=b or b=c or c=a then"Isosceles" else "Scalene" end
from triangles

-- Query the average population for all cities in CITY, rounded down to the nearest integer.
select floor(avg(population))
from city

-- The sum of all values in LAT_N rounded to a scale of  decimal places.
select round(sum(lat_n),2),round(sum(long_w),2)
from station

-- Query the sum of Northern Latitudes (LAT_N) from STATION having values greater than  and less than . Truncate your answer to  decimal places.
select truncate(sum(lat_n),4)
from station
where lat_n>38.7880 and lat_n<137.2345

-- Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than . Round your answer to  decimal places.
select round(long_w,4)
from station 
where lat_n in 
(select max(lat_n)
from station
where lat_n<137.2345)

-- median
select round(S.LAT_N,4) median
from station S 
where (select count(Lat_N) from station where Lat_N < S.LAT_N )= 
    (select count(Lat_N) from station where Lat_N > S.LAT_N)

-- Given the CITY and COUNTRY tables, query the names of all the continents (COUNTRY.Continent) and their respective average city populations (CITY.Population) rounded down to the nearest integer
select continent,floor(avg(city.population))
from city
inner join country on city.countrycode=country.code
where city.id is not null
group by continent

SELECT h.hacker_id, h.name
    FROM submissions s
    JOIN challenges c
        ON s.challenge_id = c.challenge_id
    JOIN difficulty d
        ON c.difficulty_level = d.difficulty_level 
    JOIN hackers h
        ON s.hacker_id = h.hacker_id
    WHERE s.score = d.score 
        AND c.difficulty_level = d.difficulty_level
    GROUP BY h.hacker_id
        HAVING COUNT(s.hacker_id) > 1
    ORDER BY COUNT(s.hacker_id) DESC, s.hacker_id ASC

-- olivander's interesting queryselect w.id, p.age, w.coins_needed, w.power 
from Wands as w 
inner join Wands_Property as p on w.code = p.code
where p.is_evil = 0 and w.coins_needed = (
    select min(coins_needed) 
    from Wands as w1 
    inner join Wands_Property as p1 on w1.code = p1.code
    where w1.power = w.power and p1.age = p.age) 
    order by w.power desc, p.age desc

