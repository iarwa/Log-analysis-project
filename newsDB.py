#!/usr/bin/env python

import psycopg2

DBNAME = "news"
query1 = """ SELECT '"' || articles.title || '"' ,
             COUNT(log.id) AS views FROM articles
             CROSS JOIN log WHERE log.path = '/article/' || articles.slug
             AND log.status = '200 OK'
             GROUP BY articles.id
             ORDER BY views DESC LIMIT 3; """
query2 = """ SELECT authors.name, COUNT(log.id) AS views FROM authors
             JOIN articles ON authors.id = articles.author
             CROSS JOIN log WHERE log.path = '/article/' || articles.slug
             AND log.status = '200 OK'
             GROUP BY authors.name
             ORDER BY views DESC; """
query3 = """ SELECT q1.day, ROUND(q2.views * 100.0 / q1.views, 2) AS error
             FROM (SELECT TRIM(trailing ' ' FROM TO_CHAR(DATE(time),
             'Month')) || ' ' ||
             TO_CHAR(DATE(time), 'DD') || ', ' ||
             TO_CHAR(DATE(time), 'YYYY') AS day,
             COUNT(id) AS views
                   FROM log
                   GROUP BY day)
             AS q1

             JOIN (SELECT TRIM(trailing ' ' FROM TO_CHAR(DATE(time),
             'Month')) || ' ' ||
             TO_CHAR(DATE(time), 'DD') || ', ' ||
             TO_CHAR(DATE(time), 'YYYY') AS day,
             COUNT(id) AS views
                   FROM log
                   WHERE status = '404 NOT FOUND'
                   GROUP BY day)
             AS q2 ON q1.day = q2.day
             WHERE ROUND(q2.views * 100.0 / q1.views, 2) > 1.00
             ORDER BY error DESC
             LIMIT 1; """


def execute_query(query):
    try:
        db = psycopg2.connect(dbname=DBNAME)
        c = db.cursor()
        c.execute(query)
        result = c.fetchall()
        db.close()
        return result
    except BaseException:
        return "Unable to connect to the database"


def get_popular_articles():

    """Return the most popular three articles of all time,
       most popular article at the top."""

    popular_articles = execute_query(query1)

    for article in popular_articles:
            print("{} -- {} views".format(article[0], article[1]))


def get_popular_authors():

    """Return the most popular article authors of all time,
       most popular author at the top."""

    popular_authors = execute_query(query2)

    for author in popular_authors:
            print("{} -- {} views".format(author[0], author[1]))


def get_error_requests():

    """Return which days with more than 1'%' of its requests lead to errors."""

    error_requests = execute_query(query3)

    for errors in error_requests:
            print("{} -- {} % errors".format(errors[0], errors[1]))


if __name__ == "__main__":
    print("**** Report Results ****\n(1)\tThe most popular three articles\n")
    get_popular_articles()
    print("\n-----------------------\n\n")
    print("(2)   The most popular article authors\n")
    get_popular_authors()
    print("\n-----------------------\n\n")
    print("(3)   Days with more than 1% of its requests lead to errors\n")
    get_error_requests()
