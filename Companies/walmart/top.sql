
select row_id == 2 from (select name, salary, row_count as row_id from salary order by salary desc limit 3);
 

WITH T as (SELECT * DENSE_RANK() over (ORDER BY Salary desc) as rnk FROM employees)
select name FROM T WHERE rnk = 2