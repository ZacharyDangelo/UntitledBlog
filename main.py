

#  IMPORT STATEMENTS
import os, sqlite3, Post
from flask import Flask
from flask import g, url_for, render_template, session, abort, request
#  END IMPORT STATEMENTS


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
    if error:  # TODO: Implement Logger.
        print("Error upon teardown.")
        print(error)


@app.route('/')
def show_timeline():
    db = get_db()
    cur = db.execute('select title, content, PostID from Posts order by PostID desc')
    entries = cur.fetchall()
    return render_template('timeline.html', entries=entries)


@app.route('/add', methods=['POST'])  # TODO:Session validation
def add_entry():
    db = get_db()
    db.execute('insert into Posts (title, content) values (?, ?)',
               [request.form['title'], request.form['content']])


@app.route('/post/<post_id>', methods=['GET'])
def view_post(post_id):
    fetched_post = Post.get_post(get_db(), post_id)
    return render_template('view_post.html', post=fetched_post)


@app.errorhandler(404)
def not_found_error():  # TODO:Create HTML template for 404 page.
    show_timeline()


if __name__ == "__main__":
    app.debug = True
    app.run()
