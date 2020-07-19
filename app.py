from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('home_page.html')
    return "Hello World!"


@app.route('/newsletter')
def newsletter_msg():
    return "this is the newsletter feature"


@app.route('/pictures')
def wall_pictures():
    return render_template('picture_wall.html')
    #return 'this is a wall of pictures'


@app.route('/wall')
def fourth_wall():
    return 'this is the fourth wall'

if __name__ == '__main__':
    app.run(debug = True)