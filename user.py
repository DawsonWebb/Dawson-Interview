import os
SECRET_KEY = os.environ.get('IN_DOCKER_CONTAINER', False)
import json
import requests

# Created
import validate


BASE_URL = "https://reqres.in/api/"


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
        elif validate.validateEMAIL(email) != True:
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
        print()
    elif 400 <= r.status_code <= 499:
        print(f'{r.json()["error"].capitalize()}')


# get_user does a GET request based on user input to get data on one user
def get_user(userID = 0):
    # Adds Users to the end of the domain
    url = BASE_URL + "users/"
    # starts off at 0 which is not a valid user therefore false
    validUser = False

    while not validUser:
        userID = validate.validateUserInput()

        # Adds user ID to the end of the URL
        urlUser = url + str(userID)

        # GET Request for the User ID provided
        r = requests.get(urlUser)

        if validate.validateJSON(r.text):
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


# sends a POST request to create a user
def create_user(name='', job=''):
    # Adds Login to the end of the domain
    url = BASE_URL + "users"

    while name == "":
        name = input("Please enter the new user's name: ")
        if name == "" or any(char.isdigit() for char in name):
            print("Please enter a valid name.\n")
            # Sets name blank incase name contained numbers
            name = ""
    
    while job == "":
        job = input("Please enter the new user's job: ")
        if job == "" or any(char.isdigit() for char in job):
            print("Please enter a valid job.\n")
            # Sets name blank incase name contained numbers
            job = ""

    # DICT to store the user's email and passwords which will POST as a JSON
    userInfo = {
        "name": name,
        "job": job
    }

    # Submitting Post Request with userInfo to attempt to create a user
    r = requests.post(url, json = userInfo)
    # print(r.text)

    if validate.validateJSON(r.text):
        print("JSON is valid.\n")
        requestJSON = r.json()
        print(f'User "{requestJSON["name"]}" with job "{requestJSON["job"]}" was created at {requestJSON["createdAt"]} with ID {requestJSON["id"]}\n')

        if SECRET_KEY:
            print("\n"+json.dumps(r.json(), indent=4))
        else:
            displayJSON = ""
            while displayJSON == "":
                displayJSON = input("Do you want to display the full JSON (y/n): ").strip().lower()
                if displayJSON != "y" and displayJSON != "n":
                    print("Please enter a valid response (y/n)\n")
                elif displayJSON == "y":
                    print("\n"+json.dumps(r.json(), indent=4))

    else:
        print("Error! JSON is invalid!")

    
# this will only delete a single user from the API
def delete_user(userID = 0):
    url = BASE_URL + "users/"

    # starts off at 0 which is not a valid user therefore false
    validUser = False

    # Loops until valid user is given
    while not validUser:
        if userID == 0:
            userID = validate.validateUserInput()

        # Adds user ID to the end of the URL
        urlUser = url + str(userID)

        r = requests.delete(urlUser)

        if 200 <= r.status_code <= 299:
            print(f'Status Code: {r.status_code} - Succes')
            validUser = True
        elif 400 <= r.status_code <= 499:
            print(f'Error {r.status_code} {r.text}')
            userID = 0
