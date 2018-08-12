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


class Post:
    def __eq__(self, other):
        try:
            if self.title != other.title:
                print(self.title)
                print(other.title)
                return False
            if self.post_date != other.post_date:
                print(self.post_date)
                print(other.post_date)
                return False
            if self.content != other.content:
                return False
            if self.tags != other.tags:
                return False
            return True
        except IOError:
            return False

    @staticmethod
    def search_posts(db_conn, search_term):
        if isinstance(db_conn, sqlite3.Connection):
            return db_conn.execute("select title,content from Posts where PostID ="+search_term).fetchall()
        else:
            print("Error opening database connection while attempting to search posts.")

    @staticmethod
    def get_comments(db_conn, post_id):
        if isinstance(db_conn, sqlite3.Connection):
            return db_conn.execute("select Poster,content from Comments where PostID="+post_id
                                   + " order by CommentID desc").fetchall()
        else:
            print("Error opening comment stream.")

    @staticmethod
    def get_tags(db_conn, post_id):
        if isinstance(db_conn, sqlite3.Connection):
            pass  # Insert sql statement here
        else:
            print("Error opening tag information.")


