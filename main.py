#TODO:everyhing

import Post
import os
from flask import Flask
from flask import render_template

app = Flask(__name__)  # Create Application instance.

#Home Page
@app.route('/')
def home_page():
    return render_template('master.html')


def main():
    print("Hello World")

if __name__ == "__main__":
    #app.config.from_envvar('FLASKR_SETTINGS',silent=True)
    app.run()