/* QUESTION
1. What are the most popular three articles of all time?
Which articles have been accessed the most?
Present this information as a sorted list with the most popular article at the top.

Example:

"Princess Shellfish Marries Prince Handsome" — 1201 views
"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
"Political Scandal Ends In Political Scandal" — 553 views
*/

/* OUTPUT
              title               | views
----------------------------------+--------
 Candidate is jerk, alleges rival | 338647
 Bears love berries, alleges bear | 253801
 Bad things gone, say good people | 170098
(3 rows)
*/

SELECT articles.title,
       count(*) AS views
FROM articles,
     log
WHERE log.path LIKE ('%' || articles.slug)
GROUP BY articles.title
ORDER BY views DESC
LIMIT 3;