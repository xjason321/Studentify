import os
import database, json, random
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
    return render_template('success.html', username=username)

# Signup Page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        username = request.form.get("new-username")
        password = request.form.get("new-password")

        database.create_database(username, password, 100, [], [])

        return redirect(url_for('success', username=username))

    return render_template('signup.html')

@app.route('/groups')
def groups():
    return render_template('groups.html')

# Route for saving selections
@app.route("/save-selections/", methods=["POST", "GET"])
def save_selections():
    if request.method == "POST":
        # NEURAL NETWORK CRAP HERE
        group = ["John: John#1234", "Jane: Jane#1219", "Alice: Alice#1921", "Bob: Bob#1290", "Eve: Eve#1234"]
        return render_template('groups.html', group=group)

    courses = ["CP Biology",
    "Honors Biology",
    "AP Biology",
    "CP Chemistry",
    "Honors Chemistry",
    "AP Chemistry",
    "Environmental Science",
    "AP Environmental Science (APES)",
    "Anatomy and Physiology",
    "CP Physics",
    "AP Physics 1",
    "AP Physics 2",
    "AP Phyiscs C: E and M",
    "Geometry",
    "Algebra 1",
    "Algebra 2",
    "Algebra 2 Honors",
    "Trigonometry",
    "Math Analysis / Precalculus",
    "Honors Math Analysis / Precalculus",
    "AP Calculus AB",
    "AP Calculus BC",
    "CP Statistics",
    "AP Statistics",
    "English 1",
    "CP English 2",
    "Honors English 2",
    "CP English 3",
    "Honors English 3",
    "CP English 4",
    "AP English Language and Composition",
    "AP English Literature",
    "Creative Writing",
    "Speech",
    "Yearbook",
    "Spanish [All Levels]",
    "AP Spanish",
    "French [All Levels]",
    "AP French",
    "American Sign Language (ASL) [All Levels]",
    "AP ASL",
    "Chinese [All Levels]",
    "AP Chinese",
    "AP Computer Science Principles",
    "AP Computer Science A",
    "Computer Science [General]",
    "Economics",
    "AP Economics",
    "Psychology",
    "AP Psychology",
    "AP Computer Graphics",
    "Computer Graphics",
    "Animation [All Levels]",
    "Video Production",
    "AP Ceramics",
    "AP Drawing and Painting",
    "Art [All Levels]",
    "AP Music Theory",
    "AP 3D Design",
    "3D Design",
    "AP 2D Design",
    "2D Design",
    "Geography",
    "World History",
    "AP World History",
    "US History",
    "APUSH",
    "AP/CP European History",
    "Geopolitics and the World Today",
    "CP Government",
    "AP Government",
    "Digital Electronics",
    "ROP Mechatronics",
    "Cyber Security",
    "IT Essentials",
    "Programming: C++",
    "Programming: C#",
    "Programming: Java",
    "Programming: JS",
    "Programming: Python",
    "Programming: Other Language"]

    selections = request.get_json()

    # Format dict of selected subjects
    dictSelectedSubjects = {}

    for selected in selections:
        dictSelectedSubjects[selected['subject']] = selected['proficiency']

    listSubjects = []
    listProficiencies = []

    for course in courses:
        if course in dictSelectedSubjects.keys():
            listSubjects.append(1)
            listProficiencies.append(int(dictSelectedSubjects[course]))
        else:
            listSubjects.append(0)
            listProficiencies.append(0)

    with open('database.json', 'r') as f:
        database = json.load(f)

    database['users'][-1]['subjects'] = listSubjects
    database['users'][-1]['subjects proficiency'] = listProficiencies
    database['users'][-1]['grade'] = random.randint(9, 12)

    with open('database.json', 'w') as f:
        json.dump(database, f)

    return "Received"

if __name__ == '__main__':
    app.run()
