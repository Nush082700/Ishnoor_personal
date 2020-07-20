from flask import Flask, render_template, request,redirect, url_for
import os

app = Flask(__name__)




@app.route('/', methods = ['GET','POST'])
def main_page():
    if request.method == 'POST':
        return redirect(url_for('wall_pictures'))
    return render_template('home_page.html')
    
    # return "Hello World!"

@app.route('/pictures',  methods = ['GET','POST'])
def wall_pictures():
    if request.method == 'POST':
        return redirect(url_for('newsletter_msg'))
    return render_template('picture_wall.html')
    #return 'this is a wall of pictures'

@app.route('/newsletter_1',  methods = ['GET','POST'])
def newsletter_msg():
    if request.method == 'POST':
        print ("this is a POST method")
        return redirect(url_for('newsletter_msg_2'))
    return render_template('newspaper.html')
    #return "this is the newsletter feature"

@app.route('/newsletter_2',  methods = ['GET','POST'])
def newsletter_msg_2():
    if request.method == 'POST':
        return redirect(url_for('fourth_wall'))
    return render_template('newspaper_1.html')
    #return "this is the newsletter feature"



@app.route('/wall')
def fourth_wall():
    return render_template('wall.html')
    # return 'this is the fourth wall'

if __name__ == '__main__':
    app.run(debug = True)