-- Lists all records of table second_table having a name value in my mysql server
-- Records are ordered in descending order
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
