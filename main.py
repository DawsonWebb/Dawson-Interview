# Readline is used to better the command line so accidental keys (ex. arrow keys) arent placed in command line 
import readline

# Created
import user


# Main method that will run
def run():
    # Using a try catch to make keyboard interruptions better visually
    try:
        selection = 0

        while selection < 1 and selection > 5:
            print("Select one of the Following:\n  1. Login\n  2. Get List of Users\n  3. Get Single User\n  4. Create a User\n  5. Delete a User")
            try:
                selection = int(input("Please enter the corresponding number: ").strip())

                if selection < 1 and selection > 5:
                    print("Please enter a valid number between 1-5")
            except ValueError:
                print("Please Enter a Number.\n")
            
            if selection == 1:
                # Working Email and Password for testing purposes "eve.holt@reqres.in" "cityslicka"
                user.login()
            elif selection == 2:
                user.get_users()
            elif selection == 3:
                user.get_user()
            elif selection == 4:
                user.create_user()
            elif selection == 5:
                user.delete_user()

    except KeyboardInterrupt:
        print('\n\nQuiting!')
        quit()
    else:
        print('\nNo exceptions are caught')


if __name__ == "__main__":
    run()