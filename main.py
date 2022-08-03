import json
import requests
import re

BASE_URL = "https://reqres.in/api/"

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

# validateEMAIL will use regular expressions to determine if the email provided is a valid email format
def validateEMAIL(email):
    # Regular Expression for email format (*@*.*)
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    # If email is valid it will print stating that and return true
    if re.fullmatch(regex, email):
        print("Email is valid\n")
        return True

    # When the email is invalid it states that and returns false
    else:
        print("Email is invalid! Please try again!\n")
        return False

def login():
    url = BASE_URL + "login"

    email = ""
    password = ""

    # Asks User in command line for their login information and loops if blank
    while email == "":
        email = input("Please enter your Email: ")

        # Prompts User when email is blank
        if email == "":
            print("ERROR! No email address was given. Please try again.\n")

        # Tests using REGEX to make sure email is properly formatted
        elif validateEMAIL(email) != True:
            email = ""

    while password == "":
        password = input("Please enter your Password: ")

        # Prompts User when email is blank
        if password == "":
            print("ERROR! No password was given. Please try again.\n")

    # # Working Email and Password for testing purposes
    # email = "eve.holt@reqres.in"
    # password = "cityslicka"

    # DICT to store the user's email and passwords
    userInfo = {
        "email": email,
        "password": password
    }

    # Submitting Post Request with userInfo to attempt to login
    r = requests.post(url, json = userInfo)

    # Test to see if request was succesful
    if r.status_code == 200:
        print("Successful Login!")
    elif r.status_code == 400:
        print(f'{r.json()["error"].capitalize()}')
        
    
    # # Print out the text and status for testing purposes
    # print(f'{r.text} - {type(r.status_code)}')


def run():
    url = 'https://reqres.in/api/users'
    r = requests.get(url)
    print(f'{r.text} - {r.status_code}')
    r = r.json()
    print(r)


if __name__ == "__main__":
    login()