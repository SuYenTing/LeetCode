/*
178. Rank Scores
Difficulty : Easy
題目來源：https://leetcode.com/problems/rank-scores/
*/

select score, dense_rank() over (order by score desc) as `Rank`
from Scores;