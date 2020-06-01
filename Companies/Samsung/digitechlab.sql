--SQL Questions:

--Question 1:
--Table Name: Transactions
--Account_number	transaction_time	Transaction_id	balance
--123	1/1/2019 8:00	101	1000
--123	1/2/2019 8:00	102	2000
--123	1/3/2019 8:00	103	3000
--789	1/4/2019 8:00	104	1000
--789	1/5/2019 8:00	105	500
--123	1/6/2019 8:00	106	4000
--
--Using the above (Transactions) dataset, come up with a SQL query to get
--Account_number	Transaction_id	balance
--123	106	4000
--789	105	500
--Expected Output


select account_number, transaction_id, balance from
    (select account_number, transaction_id, balance, RANK() over
        (partition by account_number order by transaction_time desc) rank from transactions) as a where a.rank = 1;



--'''Question 2:
--Table Name : Student   Table Name : Student_info
--Studentid	Subject	Marks
--1	English	80
--1	Maths	70
--1	Science	75
--1	English	85
--2	English	35
--3	English	100
--3	Maths	39
--Studentid	DOB	Location
--1	1/1/1993	Chennai
--3	1/1/1993	Bangalore
--
--Expected output
--Studentid
--2
--
--Using the above 2 tables, Write a SQL to get the list of students, for whom student_info table doesn’t have data?
--Note: without using “not in” Clause
--'''

select a.studentid from student a left join student_info b on a.studentid = b.studentid where b.studentid is null


--Question 3
--Product Code	Quantity	Inventory Date	Cumulative Sum (output)
--P1	10	1 Aug 2019	10
--P1	50	2 Aug 2019	60
--P1	20	3 Aug 2019	80
--P1	10	4 Aug 2019	90
--P2	200	1 Aug 2019	200
--P2	            350	2 Aug 2019	550
--P2	400	3 Aug 2019	950
--P3	600	1 Aug 2019	600
--P3	250	2 Aug 2019	850
--Product Inventory Table
--
--Using the above inventory dataset, Write a SQL query to get the cumulative sum (mentioned above) ordered by inventory date.


select * from product_inventory order by inventory_date asc;