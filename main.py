"""NEEDED FOR GOOGLE CLOUD"""
import os
from flask import Flask, request, send_from_directory


from python import app as App
from python import db


app = Flask(__name__, static_folder="./build", static_url_path='/')

# @todo for local
@app.before_first_request
def init_db():
    db.create_tables()



@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

# Landing page
# @todo: for now, single end point receives the quiz data
@app.route('/csv', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return App.post(request.get_json())
    if request.method == 'GET':
        return App.get()