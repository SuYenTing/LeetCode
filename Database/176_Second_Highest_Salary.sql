/*
176. Second Highest Salary
Difficulty : Easy
題目來源：https://leetcode.com/problems/second-highest-salary/
*/

# 我自己的解法
select(select Salary as SecondHighestSalary
    from(select Salary, rank() over (order by Salary desc) my_rank
         from Employee ) as t
    where my_rank = 2 limit 1) as SecondHighestSalary
from dual;

# 討論區提供解法
SELECT 
    IFNULL(
        (SELECT Distinct Salary
        FROM Employee
        ORDER BY Salary Desc
        LIMIT 1 OFFSET 1),
        NULL
    ) as SecondHighestSalary