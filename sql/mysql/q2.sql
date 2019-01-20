create table f_r(s_id int not null, s_t_i int not null,request_date varchar(15) not null);

create table r_a(r_id int not null, a_id int not null,accept_date varchar(15) not null);

insert into f_r values(1,2,"2016_06-01"),(1,3,"2016_06-01"),(1,4,"2016_06-01"),(2,3,"2016_06-02"),(3,4,"2016-06-09");

insert into r_a values(1,2,"2016_06-03"),(1,3,"2016-06-08"),(2,3,"2016-06-08"),(3,4,"2016-06-09"),(3,4,"2016-06-10");

SET @rec_req_cnt := (select count(*) from (select distinct r_id,a_id from r_a)); select @rec_req_cnt;