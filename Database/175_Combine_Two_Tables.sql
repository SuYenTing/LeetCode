/*
175. Combine Two Tables
Difficulty : Easy
題目來源：https://leetcode.com/problems/combine-two-tables/
*/

select FirstName, LastName, City, State
from Person
left join Address on Person.PersonId = Address.PersonId;