-- Lists number of records with the same score in table second_table in my mysql server
-- Records are ordered by descending order
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
