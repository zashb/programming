use db_play;

CREATE TABLE IF NOT EXISTS temp1 (
    col1 VARCHAR(30)
);
insert into temp1 values("abc123"),("xy45"),("def6"),("z9");

SELECT 
    *
FROM
    temp1;

SELECT 
    @col:=col1 AS col,
    @rev:=REVERSE(@col) AS rev,
    @rev_recast:=CAST(@rev AS UNSIGNED) AS rev_recast,
    @rev_recast_rev:=REVERSE(@rev_recast) AS num,
    SUBSTRING_INDEX(@col, @rev_recast_rev, 1) AS word
FROM
    temp1;

SELECT 
    col1
FROM
    temp1
WHERE
    col1 REGEXP '[^A-Za-z0-9]' = 0;
    
########################################################################################

CREATE TABLE IF NOT EXISTS temp2 (
    col1 VARCHAR(50)
);
insert into temp2 values("Steve Waugh"),("Mark Waugh"),("Hello World");
SELECT 
    *
FROM
    temp2;
SELECT 
    SUBSTR(SUBSTRING_INDEX(name, ' ', 1),
        1,
        1) AS a,
    SUBSTR(SUBSTRING_INDEX(name, ' ', - 1),
        1,
        1) AS b
FROM
    (SELECT 
        col1 AS name
    FROM
        temp2
    WHERE
        col1 LIKE '%Steve%') AS x;
########################################################################################
