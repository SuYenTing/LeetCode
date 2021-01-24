/*
196. Rising Temperature
Difficulty : Easy
題目來源：https://leetcode.com/problems/rising-temperature/
*/

select a.id
from Weather as a
join Weather as b on a.recordDate = b.recordDate + interval 1 day
where a.Temperature > b.Temperature