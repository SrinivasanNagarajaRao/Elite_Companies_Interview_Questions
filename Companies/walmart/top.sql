
select row_id == 2 from (select name, salary, row_count as row_id from salary order by salary desc limit 3);