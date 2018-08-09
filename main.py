

import Post
import os, sqlite3
from flask import Flask
from flask import g,url_for, render_template,session, abort, request

app = Flask(__name__, instance_path='/instanceFiles')  # Create Application instance.


def connect_db():
    conn = sqlite3.connect(os.path.join(app.instance_path, 'db.db'))
    conn.row_factory = sqlite3.Row
    return conn


def get_db():
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
        return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select title, content from Post order by id desc')
    entries = cur.fetchall()
    return render_template(url_for('timeline.html', entries=entries))


@app.route('/add', methods=['POST'])  # TODO:Session validation
def add_entry():
    db = get_db()
    db.execute('insert into Post (title, content) values (?, ?)',
               [request.form['title'], request.form['content']])


def main():
    print("Hello World")


if __name__ == "__main__":
    app.run()
