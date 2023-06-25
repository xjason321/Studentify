"""
LING HACKS V - June 24th to 25th

Idea: Translate images of Sign Language to text
Description: Takes images of hands and returns. 

Coders: Jason Xie, Subhash Srinivasa, Komal Tummala
"""
<<<<<<< Updated upstream
import os
# import openai
# openai.api_key = os.environ["OPENAI_API_KEY"]

from flask import Flask, render_template, request, redirect, url_for
import database
=======
import json
from flask import Flask, render_template, request, redirect, url_for, session
>>>>>>> Stashed changes

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
@app.route('/login')
def login():
    return render_template('login.html')

# Success Page
@app.route('/user/profile/<username>', methods=['GET'])
def success(username):
    return render_template('success.html', user=username)

# Signup Page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        username = request.form.get("new-username")
        password = request.form.get("new-password")

        formatdata = {
            'name': username,
            'password': password,
        }

        write_json(formatdata, "database.json")

        return redirect(url_for('success', username=username))

    return render_template('signup.html')

if __name__ == '__main__':
    app.run()
