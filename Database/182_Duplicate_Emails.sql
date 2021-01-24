/*
182. Duplicate Emails
Difficulty : Easy
題目來源：https://leetcode.com/problems/duplicate-emails/
*/

# 我的寫法
select distinct a.Email
from Person as a
join Person as b on a.Email = b.Email
where a.Id != b.Id;

# group by寫法
select Email
from Person
group by Email
having count(*) > 1;