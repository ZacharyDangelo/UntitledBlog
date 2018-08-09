"""
This file contains the class that handles Posts.
Uses flat JSON files to store posts. database is not needed.
TODO:Find a good file naming convention
TODO:CONSISTENT CODE STYLE.
FOLLOW PEP8.


One thing to think about, should the JSON file contain the content itself, or simply a path to the .html file?
Probably the latter if i had to guess. This allows faster parsing of the JSON for the purpose of ordering posts
as well as just more abstraction and encapsulation?
"""
import jsonpickle
import datetime as dt


class Post:
    tags = []
    title = ''
    post_date = ''
    content = ''

    def __init__(self,title="DefaultTitle",content="DefaultContent"):
        self.title=title
        self.content=content
        post_date = str(dt.datetime.now())

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
