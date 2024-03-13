-- groups number using scores
SELECT score, COUNT(*) AS num
FROM second_table
GROUP BY score
ORDER BY num DESC;
