import json
import requests
# Library for regex
import re
# Readline is used to better the command line so accidental keys (ex. arrow keys) arent placed in command line 
import readline 


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
        # print("Email is valid\n")
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

    # Printing a newline for command line formating purposes
    print()

    # # Working Email and Password for testing purposes
    # email = "eve.holt@reqres.in"
    # password = "cityslicka"

    # DICT to store the user's email and passwords which will POST as a JSON
    userInfo = {
        "email": email,
        "password": password
    }

    # Submitting Post Request with userInfo to attempt to login
    r = requests.post(url, json = userInfo)

    # Test to see if request was succesful
    if 200 <= r.status_code <= 299:
        print("Successful Login!")
    # Test to see if request was incorrect
    elif 400 <= r.status_code <= 499:
        print(f'{r.json()["error"].capitalize()}')


# Main method that will run
def run():
    # Using a try catch to make keyboard interruptions better visually
    try:
        login()
    except KeyboardInterrupt:
        print('\n\nQuiting!')
        quit()
    else:
        print('No exceptions are caught')


if __name__ == "__main__":
    run()