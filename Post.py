"""
This class will contain methods for interacting with Posts on the site.
Need to plan out how I want to do that, and whether we need other classes as well.

Maybe there is a need to think of it as

Presentation Layer
Logic Layer
Data Layer

??? does this thinking work ???
"""

#  IMPORT STATEMENTS
import datetime as dt
import sqlite3
#  END IMPORTS


def search_posts(db_conn, search_term):
    if isinstance(db_conn, sqlite3.Connection):
        return db_conn.execute("select title,content from Posts where PostID ="+search_term).fetchall()
    else:
        print("Error opening database connection while attempting to search posts.")


def get_comments(db_conn, post_id):
    if isinstance(db_conn, sqlite3.Connection):
        return db_conn.execute("select Poster,content from Comments where PostID="+post_id
                                   + " order by CommentID desc").fetchall()
    else:
        print("Error opening comment stream.")


def get_tags(db_conn, post_id):
    if isinstance(db_conn, sqlite3.Connection):
        pass  # Insert sql statement here
    else:
        print("Error opening tag information.")


def get_post(db_conn, post_id):
    curr = db_conn.execute('select title, content from Posts where PostID =' + post_id)
    fetched_post = curr.fetchall()[0]
    return fetched_post
