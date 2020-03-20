import json
import re
from datetime import datetime

import pytz
from flask import Flask, request, render_template, jsonify

import db

app = Flask(__name__)

def parse_tags(post):
    pat = r'(\#{1}[\w\d]{2,20})'
    s = re.findall(pat, post)
    return ';'.join(s)

def parse_ats(post):
    pat = r'(\@{1}[\w\d]{5,30})'
    s = re.findall(pat, post)
    return ';'.join(s)

@app.route('/', methods=['GET','POST'])
def index():

    if request.method=='GET':
        print('handle GET')
        pass

    if request.method=='POST':
        print('handle POST')
        user = request.form['user']
        post = request.form['post']
        parent = request.form['parent']
        item = request.form['item']
        location = request.form['location']

        created = datetime.now(tz=pytz.utc)

        tags = parse_tags(post)
        ats = parse_ats(post)
        status = 1

        db.create_post(user, post, parent, location, item, tags, ats, created, status)

    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)