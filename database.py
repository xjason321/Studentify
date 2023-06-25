import json
import requests

def create_database(username, password):
    try:
        # Read the existing database file
        with open('database.json', 'r') as f:
            database = json.load(f)
    except FileNotFoundError:
        # If the file doesn't exist, create an empty database
        database = {}
        database['users'] = []

    # Append the new user to the 'users' list
    database['users'].append({
        'username': username,
        'password': password
    })

    # Write the updated database back to the file
    with open('database.json', 'w') as f:
        json.dump(database, f)

def main():
    username = input('Enter username: ')
    password = input('Enter password: ')

    create_database(username, password)

if __name__ == '__main__':
    main()


def extract_input(html_file, id):
    response = requests.get(html_file)
    soup = bs4.BeautifulSoup(response.content, 'html.parser')

    input_tag = soup.find(id=id)
    input_value = input_tag['value']

    return input_value