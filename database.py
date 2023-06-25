import json
import random
def create_database(username, password):
     try:
         # Read the aexisting database file
         with open('database.json', 'r') as f:
             database = json.load(f)
     except FileNotFoundError:
         # If the file doesn't exist, create an empty database
         database = {}
         database['users'] = []

     database['users'].append({'username':username, 'passwword': password})
     sublist = []
     proflist = []
     for i in range(13):
         sublist.append(random.randint(0,1))
         if sublist[i] == 0:
             proflist.append(0)
         else:
             proflist.append(random.randint(0,5))
     database['users'][-1]['subjects'] = sublist
     database['users'][-1]['subjects proficiency'] = proflist
     with open('database.json', 'w') as f:
         json.dump(database, f)

def main():
    username = input('Enter username: ')
    password = input('Enter password: ')

    create_database(username, password)

if __name__ == '__main__':
    main()
