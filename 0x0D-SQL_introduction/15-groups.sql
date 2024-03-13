-- groups number using scores
SELECT scores COUNT(*) AS num
FROM second_table
GROUP BY scores
ORDER BY number DESC, scores DESC;
