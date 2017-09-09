/* QUESTION
2. Who are the most popular article authors of all time?
That is, when you sum up all of the articles each author has written,
which authors get the most page views? Present this as a sorted list
with the most popular author at the top.

Example:

Ursula La Multa — 2304 views
Rudolf von Treppenwitz — 1985 views
Markoff Chaney — 1723 views
*/

/* OUTPUT
         author         | total_views
------------------------+-------------
 Ursula La Multa        |      507594
 Rudolf von Treppenwitz |      423457
 Anonymous Contributor  |      170098
 Markoff Chaney         |       84557
(4 rows)
*/

SELECT author,
       sum(views) AS total_views
FROM
  (SELECT authors.name AS author,
          article_views.title,
          article_views.views
   FROM authors,
        articles,
        article_views
   WHERE articles.author = authors.id
     AND article_views.title = articles.title
   ORDER BY article_views.views DESC) author_title_views
GROUP BY author
ORDER BY total_views DESC;