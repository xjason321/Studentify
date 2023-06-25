"""
LING HACKS V - June 24th to 25th

Idea: Translate images of Sign Language to text
Description: Takes images of hands and returns. 

Coders: Jason Xie, Subhash Srinivasa, Komal Tummala
"""
import os
# import openai
# openai.api_key = os.environ["OPENAI_API_KEY"]

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder='static')

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
        return redirect(url_for('user/profile/placeholder'))

    return render_template('signup.html')

if __name__ == '__main__':
    app.run()
