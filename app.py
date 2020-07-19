from flask import Flask, render_template

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
    return render_template('wall.html')


if __name__ == "__main__":
    app.run(debug=True)
