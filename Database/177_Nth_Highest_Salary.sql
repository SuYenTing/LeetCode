/*
177. Nth Highest Salary
Difficulty : Easy
題目來源：https://leetcode.com/problems/nth-highest-salary/
*/

# 第一種解法
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      
      select Salary
      from(select Salary, rank() over (order by Salary desc) my_rank
           from(select distinct Salary
                from Employee 
                order by Salary desc) as t1) as t2
      where my_rank = N
      
  );
END


# 第二種解法
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT

BEGIN
    SET N=N-1;
  RETURN (
      select distinct salary 
      from employee 
      order by salary 
      desc limit N,1
  );
END