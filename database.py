import json

def create_database(username, password):
     try:
         # Read the aexisting database file
         with open('database.json', 'r') as f:
             database = json.load(f)
     except FileNotFoundError:
         # If the file doesn't exist, create an empty database
         database = {}
         database['users'] = {}

     database['users']['username'] = username
     database['users']['password'] = password

     with open('database.json', 'w') as f:
         json.dump(database, f)

def main():
    username = input('Enter username: ')
    password = input('Enter password: ')

    create_database(username, password)

if __name__ == '__main__':
    main()
