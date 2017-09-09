/*
The following script creates three views:

1. article_views
2. log_errors
3. log_visits

This script needs to be run before executing the python code.
*/

CREATE VIEW article_views AS
SELECT articles.title,
       count(*) AS views
FROM articles,
     log
WHERE log.path LIKE ('%' || articles.slug)
GROUP BY articles.title
ORDER BY views DESC;


CREATE VIEW log_errors AS
SELECT date_trunc('day', time) AS DAY,
       count(status) AS errors
FROM log
WHERE status LIKE '%404%'
GROUP BY DAY
ORDER BY DAY;


CREATE VIEW log_visits AS
SELECT date_trunc('day', time) AS DAY,
       count(status) AS visits
FROM log
GROUP BY DAY
ORDER BY DAY;