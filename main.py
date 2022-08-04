# Readline is used to better the command line so accidental keys (ex. arrow keys) arent placed in command line 
import readline

# Created
import user


# Main method that will run
def run():
    # Using a try catch to make keyboard interruptions better visually
    try:
        # Working Email and Password for testing purposes "eve.holt@reqres.in" "cityslicka"
        # login()
        # get_users()
        # get_user()
        # create_user()
        user.delete_user()
    except KeyboardInterrupt:
        print('\n\nQuiting!')
        quit()
    else:
        print('\nNo exceptions are caught')


if __name__ == "__main__":
    run()