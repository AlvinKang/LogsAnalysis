#!/usr/bin/env python

import psycopg2

# SQL script for Question 1
script1 = '''
SELECT articles.title,
       count(*) AS views
FROM articles,
     log
WHERE log.path LIKE ('%' || articles.slug)
GROUP BY articles.title
ORDER BY views DESC
LIMIT 3;
'''

# SQL script for Question 2
script2 = '''
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
'''

# SQL script for Question 3
script3 = '''
SELECT *
FROM
  (SELECT log_errors.day,
          log_errors.errors/cast(log_visits.visits AS float) AS errors_ratio
   FROM log_errors,
        log_visits
   WHERE log_errors.day = log_visits.day
   ORDER BY errors_ratio DESC) log_ratio
WHERE errors_ratio > 0.01;
'''

# Define functions used


def run_script(cursor, script):
    cursor.execute(script)
    return cursor.fetchall()


def format_script1(outputs):
    '''
    SQL output:
    3 rows: (title, views)

    Target output format:
    "Princess Shellfish Marries Prince Handsome" - 1201 views
    "Baltimore Ravens Defeat Rhode Island Shoggoths" - 915 views
    "Political Scandal Ends In Political Scandal" - 553 views
    '''
    formatted_output = ""

    for entry in outputs:
        title = entry[0]
        views = entry[1]
        format_string = "\"{}\" - {} views\n".format(title, views)
        formatted_output += format_string

    return formatted_output


def format_script2(outputs):
    '''
    SQL output:
    4 rows: (author, total_views)

    Target output format:
    Ursula La Multa - 2304 views
    Rudolf von Treppenwitz - 1985 views
    Markoff Chaney - 1723 views
    '''
    formatted_output = ""

    for entry in outputs:
        author = entry[0]
        total_views = entry[1]
        format_string = "\"{}\" - {} views\n".format(author, total_views)
        formatted_output += format_string

    return formatted_output


def format_script3(outputs):
    '''
    SQL output:
    1 rows: (day (timestamp), errors_ratio (float))

    Target output format:
    July 29, 2016 - 2.5% errors
    '''
    formatted_output = ""

    dt = outputs[0][0].strftime("%B %d, %Y")
    percent = "{0:.1f}% errors".format(outputs[0][1] * 100)
    formatted_output = "{} - {}\n".format(dt, percent)
    return formatted_output


def print_border():
    print("\n")
    print("==================================================================")
    print("\n\n")

# Execute SQL scripts and print results
db = psycopg2.connect(database="news")
c = db.cursor()

title = '''
\n\t\t\t LOG ANALYSIS'''
print(title)
print_border()

# Question 1 and response
question1 = '''QUESTION 1:

What are the most popular three articles of all time?
Which articles have been accessed the most?\n'''

print(question1)
results1 = run_script(c, script1)
print(format_script1(results1))
print_border()

# Question 2 and response
question2 = '''QUESTION 2:

Who are the most popular article authors of all time?\n'''

print(question2)
results2 = run_script(c, script2)
print(format_script2(results2))
print_border()

# Question 3 and response
question3 = '''QUESTION 3:

On which days did more than 1% of requests lead to errors?\n'''

print(question3)
results3 = run_script(c, script3)
print(format_script3(results3))
print_border()

db.close()
