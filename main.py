

import Post
import os, sqlite3
from flask import Flask
from flask import g,url_for, render_template,session, abort, request

app = Flask(__name__)  # Create Application instance.


def connect_db():
    conn = sqlite3.connect('instanceFiles/db.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
        return g.sqlite_db
    else:
        print("Error in get_db()")


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
    if error:  # Should we have a logger?
        print("Error upon teardown.")
        print(error)


@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select title, content from Posts order by PostID desc')
    entries = cur.fetchall()
    return render_template('timeline.html', entries=entries)


@app.route('/add', methods=['POST'])  # TODO:Session validation
def add_entry():
    db = get_db()
    db.execute('insert into Posts (title, content) values (?, ?)',
               [request.form['title'], request.form['content']])


def main():
    print("Hello World")


if __name__ == "__main__":
    app.debug = True
    app.run()
