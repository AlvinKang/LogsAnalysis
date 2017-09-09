/* QUESTION
3. On which days did more than 1% of requests lead to errors?
The log table includes a column status that indicates the HTTP
status code that the news site sent to the user's browser.
(Refer back to this lesson if you want to review the idea of HTTP status codes.)

Example:

July 29, 2016 — 2.5% errors
*/

/* OUTPUT
          day           |    errors_ratio
------------------------+--------------------
 2016-07-17 00:00:00+00 | 0.0226268624680273
(1 row)
*/

SELECT *
FROM
  (SELECT log_errors.day,
          log_errors.errors/cast(log_visits.visits AS float) AS errors_ratio
   FROM log_errors,
        log_visits
   WHERE log_errors.day = log_visits.day
   ORDER BY errors_ratio DESC) log_ratio
WHERE errors_ratio > 0.01;