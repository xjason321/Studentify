"""
LING HACKS V - June 24th to 25th

Idea: Translate images of Sign Language to text
Description: Takes images of hands and returns. 

Coders: Jason Xie, Subhash Srinivasa, Komal Tummala
"""

from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
