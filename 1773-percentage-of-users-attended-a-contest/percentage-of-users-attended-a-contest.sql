# Write your MySQL query statement below
select r.contest_id, 
round(count(distinct r.user_id)*100 / (select count(*) from users),2) as percentage
from register  r
group by r.contest_id 
order by percentage DESC, contest_id ASC;

-- SELECT
--     r.contest_id,
--     ROUND(
--         COUNT(DISTINCT r.user_id) * 100 /
--         (SELECT COUNT(*) FROM Users),
--         2
--     ) AS percentage
-- FROM Register r
-- GROUP BY r.contest_id
-- ORDER BY percentage DESC, contest_id ASC;
