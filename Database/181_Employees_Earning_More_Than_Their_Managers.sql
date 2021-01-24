/*
181. Employees Earning More Than Their Managers
Difficulty : Easy
題目來源：https://leetcode.com/problems/employees-earning-more-than-their-managers/
*/

select a.Name as Employee
from Employee as a
join Employee as b on a.ManagerId = b.Id
where a.Salary > b.Salary;