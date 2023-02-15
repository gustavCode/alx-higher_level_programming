-- a script that displays the max temperature
-- of each state (ordered by State name)

SELECT state, MAX(value) AS `max_value`
FROM temperatures GROUP BY state
ORDER BY state ASC;
