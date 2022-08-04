# Library for regex
import re
import json

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


def validateUserInput(userID=0):
    while userID < 1:
        # Try Catch to ensure it is a int not string
        try:
            userID = int(input("Enter the User ID: "))

            # States to User when Value is below 1 since IDs start at 1
            if userID < 1:
                print("Please Enter a Valid User ID.\n")
        except ValueError:
            print("Please Enter a Number.\n")
    return userID