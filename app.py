from flask import Flask

app = Flask(__name__)


@app.route('/')
def main_page():
    return "Hello World!"


@app.route('/newsletter')
def newsletter_msg():
    return "this is the newsletter feature"


@app.route('/pictures')
def wall_pictures():
    return 'this is a wall of pictures'


@app.route('/wall')
def fourth_wall():
    return 'this is the fourth wall'
