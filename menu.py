"""
Provides a basic frontend
"""
import sys
import logging
import main
import user_status
from user_status import UserStatusCollection
from users import UserCollection


# Configure the logging module
logging.basicConfig(filename='log_07_20_2023.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def load_users():
    """
    Loads user accounts from a file
    """
    logging.info('Loading user accounts from a file')
    filename = input('Enter filename of user file: ')
    main.load_users(filename, user_collection)


def load_status_updates():
    """
    Loads status updates from a file
    """
    logging.info('Loading status updates from a file')
    filename = input('Enter filename for status file: ')
    main.load_status_updates(filename, status_collection)


def add_user():
    """
    Adds a new user into the database
    """
    logging.info('Adding new user account to a file')
    user_id = input('User ID: ')
    email = input('User email: ')
    user_name = input('User name: ')
    user_last_name = input('User last name: ')
    if not main.add_user(user_id,
                         email,
                         user_name,
                         user_last_name,
                         user_collection):
        print("An error occurred while trying to add new user")
    else:
        print("User was successfully added")


def update_user():
    """
    Updates information for an existing user
    """
    logging.info('Updating user account for an existing user to a file')
    user_id = input('User ID: ')
    email = input('User email: ')
    user_name = input('User name: ')
    user_last_name = input('User last name: ')
    if not main.update_user(user_id, email, user_name, user_last_name, user_collection):
        print("An error occurred while trying to update user")
    else:
        print("User was successfully updated")


def search_user(user_collection):
    """
    Searches a user in the database
    """
    logging.info('Searching for a user in a file')
    user_id = input('Enter user ID to search: ')
    result = main.search_user(user_id, user_collection)
    if not result.user_id:
        print("ERROR: User does not exist")
    else:
        print(f"User ID: {result.user_id}")
        print(f"Email: {result.email}")
        print(f"Name: {result.user_name}")
        print(f"Last name: {result.user_last_name}")


def delete_user():
    """
    Deletes user from the database
    """
    logging.info('Deleting a user account from a file')
    user_id = input('User ID: ')
    if not main.delete_user(user_id, user_collection):
        print("An error occurred while trying to delete user")
    else:
        print("User was successfully deleted")


def save_users():
    """
    Saves user database into a file
    """
    logging.info('Saving user information to a file')
    filename = input('Enter filename for users file: ')
    main.save_users(filename, user_collection)


def add_status():
    """
    Adds a new status into the database
    """
    logging.info('Adding a new status for a user')
    user_id = input('User ID: ')
    status_id = input('Status ID: ')
    status_text = input('Status text: ')
    # Create an instance of UserStatusCollection
    status_collection_instance = UserStatusCollection()
    # Call the add_status function on the status_collection instance
    if not status_collection.add_status(user_id, status_id, status_text):
        print("An error occurred while trying to add new status")
    else:
        print("New status was successfully added")


def update_status():
    """
    Updates information for an existing status
    """
    logging.info('Updating existing status')
    user_id = input('User ID: ')
    status_id = input('Status ID: ')
    status_text = input('Status text: ')
    if not main.update_status(user_id, status_id, status_text, status_collection):
        print("An error occurred while trying to update status")
    else:
        print("Status was successfully updated")


def search_status():
    """
    Searches a status in the database
    """
    logging.info('Searching a status for a user')
    status_id = input('Enter status ID to search: ')
    result = main.search_status(status_id, status_collection)
    if not result.status_id:  # Check if status was not found
        print("ERROR: Status does not exist")
    else:
        print(f"User ID: {result.user_id}")
        print(f"Status ID: {result.status_id}")
        print(f"Status text: {result.status_text}")


def delete_status():
    """
    Deletes status from the database
    """
    logging.info('Deleting a user status')
    status_id = input('Status ID: ')
    if not main.delete_status(status_id, status_collection):
        print("An error occurred while trying to delete status")
    else:
        print("Status was successfully deleted")


def save_status():
    """
    Saves status database into a file
    """
    logging.info('Saving a user status to a file')
    filename = input('Enter filename for status file: ')
    main.save_status_updates(filename, status_collection)


def quit_program():
    """
    Quits program
    """
    logging.info('quiting program')
    sys.exit()


if __name__ == '__main__':
    user_collection = main.init_user_collection()
    status_collection = main.init_status_collection()
    menu_options = {
        'A': load_users,
        'B': load_status_updates,
        'C': add_user,
        'D': update_user,
        'E': search_user,
        'F': delete_user,
        'G': save_users,
        'H': add_status,
        'I': update_status,
        'J': search_status,
        'K': delete_status,
        'L': save_status,
        'Q': quit_program
    }
    while True:
        user_selection = input("""
                            A: Load user database
                            B: Load status database
                            C: Add user
                            D: Update user
                            E: Search user
                            F: Delete user
                            G: Save user database to file
                            H: Add status
                            I: Update status
                            J: Search status
                            K: Delete status
                            L: Save status database to file
                            Q: Quit

                            Please enter your choice: """)
        user_selection = user_selection.strip().upper()  # Convert input to uppercase and remove leading/trailing spaces
        if user_selection.upper() in menu_options:
            menu_options[user_selection]()
        else:
            print("Invalid option")
