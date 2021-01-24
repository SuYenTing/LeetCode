/*
196. Delete Duplicate Emails
Difficulty : Easy
題目來源：https://leetcode.com/problems/delete-duplicate-emails/
*/

delete from Person 
where id in (select id from (select a.id 
             from Person as a
             join Person as b on a.Email = b.Email and a.id > b.id) as t);