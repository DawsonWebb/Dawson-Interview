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


# login will take user input and send a POST request
def login(email='', password=''):
    # Adds Login to the end of the domain
    url = BASE_URL + "login"

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
    else:
        print(f'{r.status_code} - {r.text}')


# get_users does a GET request to get the first page of user info and to see total pages
# using total pages it sets the max pages to iterate through and grab all of the user data
def get_users():
    # Adds Users to the end of the domain
    url = BASE_URL + "users"

    # GET Request for the first page of Users
    r = requests.get(url)
    # Change the request type to JSON in a new variable
    requestJSON = r.json()
    
    # Test to ensure a succesful GET request was performed
    if 200 <= r.status_code <= 299:
        print("Succesful Response on Page 1")
        # Creating an User Dict to store the total number of users/pages as well as the user data
        users = {
            "total": 0,
            "total_pages": 0,
            "data": []
        }

        # Adds the 1st page of user data to the user dict
        users["data"] += requestJSON["data"]
        # Takes the Total Users and Total Pages given by the 1st page into the User Dict
        users["total"] = r.json()["total"]
        users["total_pages"] = r.json()["total_pages"]

        # For loop to itterate through every possible page of users to pull every user data
        for x in range(1, users["total_pages"]):
            # Takes the users url and adds the page numbers
            extraUrl = url + "?page=" + str(x+1)
            # Perform a get request using the user page url
            newR = requests.get(extraUrl)
            # Converts request class type to json type
            newRJson = newR.json()

            # Checks status code for a succesful GET request
            if 200 <= newR.status_code <= 299:
                print(f'Succesful Response on Page {x+1}')
                # Adds the User data from the current page to the existing Users dict
                users["data"] += newRJson["data"]
            elif 400 <= newR.status_code <= 499:
                print(f'{newR.status_code}: {newRJson["error"].capitalize()}')
        
        # Prints out Total Users and Pages
        print(f'\nTotal Users Found: {users["total"]}\nTotal Pages: {users["total_pages"]}')
    elif 400 <= r.status_code <= 499:
        print(f'{r.json()["error"].capitalize()}')


# get_user does a GET request based on user input to get data on one user
def get_user():
    # Adds Login to the end of the domain
    url = BASE_URL + "users/"
    # Sets userID to 0 since no userID is 0
    userID = 0
    # starts off at 0 which is not a valid user
    validUser = False

    while not validUser:
        # Asks User for a valid User ID
        while userID < 1:
            # Try Catch to ensure it is a int not string
            try:
                userID = int(input("Enter the User ID: "))

                # States to User when Value is below 1 since IDs start at 1
                if userID < 1:
                    print("Please Enter a Valid User ID.\n")
            except ValueError:
                print("Please Enter a Number.\n")

        # Adds user ID to the end of the URL
        urlUser = url + str(userID)

        # GET Request for the User ID provided
        r = requests.get(urlUser)

        if validateJSON(r.text):
            # Change the request type to JSON in a new variable
            requestJSON = r.json()

            if len(requestJSON) > 0 and 200 <= r.status_code <= 299:
                validUser = True
                # Print JSON data into a user friendly format
                print(f'Found User: {requestJSON["data"]["first_name"]} {requestJSON["data"]["last_name"]} {requestJSON["data"]["email"]} ({requestJSON["data"]["id"]})')
            elif 400 <= r.status_code <= 499:
                userID = 0
                print("User not found. Please try again.\n")

            # print(requestJSON)
            # print()
                
        else:
            print("Invalid JSON")
    


# Main method that will run
def run():
    # Using a try catch to make keyboard interruptions better visually
    try:
        # Working Email and Password for testing purposes "eve.holt@reqres.in" "cityslicka"
        # login()
        # get_users()
        get_user()
    except KeyboardInterrupt:
        print('\n\nQuiting!')
        quit()
    else:
        print('\nNo exceptions are caught')


if __name__ == "__main__":
    run()