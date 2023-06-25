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
    return redirect(url_for('login', success="~"))

# Login Page
@app.route('/login/<success>', methods=['GET', 'POST'])
def login(success="~"):
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        listOfUsers = []

        # Generate list of user-pass combos in database
        with open('database.json') as f:
            compositedata = json.load(f)
            for user in compositedata["users"]:
                listOfUsers.append([user["username"], user["password"]])

        # If entered combo in database
        if [username, password] in listOfUsers:
            return redirect(url_for('success', username=username))
        else:
            return redirect(url_for('login', success="false"))

    return render_template('login.html', success=success)

# Success Page
@app.route('/user/profile/<username>', methods=['GET', 'POST'])
def success(username):
    return render_template('filters.html')

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
