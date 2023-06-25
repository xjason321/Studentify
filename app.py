"""
LING HACKS V - June 24th to 25th

Idea: Translate images of Sign Language to text
Description: Takes images of hands and returns. 

Coders: Jason Xie, Subhash Srinivasa, Komal Tummala
"""
import os
import database
import json
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__, static_folder='static')

# function to add to JSON
def write_json(newdata, filename='data.json'):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)  # Load existing data from the file
    except FileNotFoundError:
        data = {}  # Create an empty dictionary if the file doesn't exist

    # Update the data dictionary with newdata
    data.setdefault('users', {}).update(newdata)

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)  # Write the updated data back to the file

# Default path
@app.route('/')
def default():
    # Redirect to the 'login' route
    return redirect(url_for('login'))

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # TODO: Make a new json file for sensitive info
        with open('database.json') as f:
            compositedata = json.load(f)
            listOfUsers = []
            for user in compositedata["users"]:
                listOfUsers.append([user["username"], user["password"]])
            print(listOfUsers)

    return render_template('login.html')

# Success Page
@app.route('/user/profile/<username>')
def success(username):
    return render_template('success.html', user=username)

# Signup Page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        username = request.form.get("new-username")
        password = request.form.get("new-password")

        database.create_database(username, password)

        return redirect(url_for('success', username=username))

    return render_template('signup.html')

if __name__ == '__main__':
    app.run()
