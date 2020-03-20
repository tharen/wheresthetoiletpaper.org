from flask import Flask, request, render_template, jsonify
import json

import db

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():

    if request.method=='GET':
        print('handle GET')
        pass

    if request.method=='POST':
        print('handle POST')
        user = request.form['user']
        post = request.form['post']
        item = request.form['item']
        location = request.form['location']

        print(user, post, location, item)
        tags = '' #parse_tags(post)
        ats = '' #parse_ats(post)

        # data.create_post(user, post, location, item, tags, ats)

    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)