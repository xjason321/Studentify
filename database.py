import json
import random

def create_database(username, password, grade, subjects, proficiencies):
     try:
         # Read the aexisting database file
         with open('database.json', 'r') as f:
             database = json.load(f)
     except FileNotFoundError:
         # If the file doesn't exist, create an empty database
         database = {}
         database['users'] = []

     database['users'].append({'username':username, 'password': password, 'grade': grade, 'subjects': subjects, 'subjects proficiency': proficiencies})

     with open('database.json', 'w') as f:
        json.dump(database, f)

def main():
    for i in range(101, 500):
        username = "bot" + str(i)
        password = "password" + str(i)
        grade = random.randint(9, 12)
        
        listSubjects = []
        listProficiencies = []
        
        for i in range(81):
            isSelected = random.randint(0, 1)
            if isSelected:
                listSubjects.append(1)
                listProficiencies.append(random.randint(1, 3))
            else:
                listSubjects.append(0)
                listProficiencies.append(0)

        create_database(username, password, grade, listSubjects, listProficiencies)

if __name__ == '__main__':
    main()
