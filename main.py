"""
This module contains functions to manage user data and status updates using CSV files.

Requirements:
- The CSV files used for loading and saving data must have specific formats.
- Some functions return True on success and False on errors, as described in their docstrings.

Note: This module depends on the 'csv', 'users', and 'user_status' modules for its functionalities.

Author: Bita Massoudi
Date: 7/25/2023
"""
import csv
import users
import user_status
import logging


def init_user_collection():
    """
    Creates and returns a new instance of UserCollection
    """
    return users.UserCollection()



def init_status_collection():
    """
    Creates and returns a new instance of UserStatusCollection
    """
    return user_status.UserStatusCollection()


def load_users(filename, user_collection_instance):
    """
    Opens a CSV file with user data and adds it to an existing instance of UserCollection

    Requirements:
    - If a user_id already exists, it will ignore it and continue to the next.
    - Returns False if there are any errors (such as empty fields in the source CSV file)
    - Otherwise, it returns True.
    """
    try:
        with open(filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if not user_collection_instance.add_user\
                            (row['user_id'], row['email'], row['name'], row['lastname']):
                    print('Error: Invalid data in CSV file')
                    return False
        return True
    except FileNotFoundError as error:
        print(f'Error: {error}')
        return False
    except KeyError as error:
        print(f'Error: {error}')
        return False


def save_users(filename, user_collection_instance):

    """
    Saves all users in user_collection into a CSV file

    Requirements:
    - If there is an existing file, it will overwrite it.
    - Returns False if there are any errors (such as an invalid filename).
    - Otherwise, it returns True.
    """
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['user_id', 'email', 'name', 'lastname'])
            for user in user_collection_instance.database.values():
                writer.writerow([user.user_id, user.email, user.user_name, user.user_last_name])
        return True
    except FileNotFoundError as error:
        print(f'Error: File not found - {error}')
        return False
    except PermissionError as error:
        print(f'Error: Permission denied - {error}')
        return False
    except csv.Error as error:
        print(f'Error: CSV related error - {error}')
        return False
    except Exception as error:
        print(f'Error: Unexpected error - {error}')
        return False

def search_status(status_id, status_collection_instance):
    """
    Searches for a status in status_collection_instance (which is an instance of UserStatusCollection).

    Requirements:
    - If the status is found, returns the corresponding UserStatus instance.
    - Otherwise, it returns None.
    """
    return status_collection_instance.search_status(status_id)


def update_status(user_id, status_id, status_text, status_collection_instance):
    """
    Updates the values of an existing status
    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    """
    return status_collection_instance.modify_status(user_id, status_id, status_text)


def delete_status(status_id, status_collection_instance):
    """
    Deletes a status from the status collection.

    Requirements:
    - Returns False if there are any errors (such as status_id not found)
    - Otherwise, it returns True.
    """
    logging.info(f"Deleting status with ID '{status_id}'.")
    if status_id not in status_collection_instance.statuses:
        logging.error(f"An error occurred while trying to delete status with ID '{status_id}'. Status ID does not exist.")
        return False

    try:
        del status_collection_instance.statuses[status_id]
        logging.info(f"Status with ID '{status_id}' deleted successfully.")
        return True
    except Exception as e:
        logging.error(f"An unexpected error occurred while trying to delete status with ID '{status_id}': {e}")
        return False



def load_status_updates(filename, status_collection_instance):
    """
    Opens a CSV file with status data and adds it to an existing instance of UserStatusCollection

    Requirements:
    - If a status_id already exists, it will ignore it and continue to the next.
    - Returns False if there are any errors (such as empty fields in the source CSV file)
    - Otherwise, it returns True.
    """
    try:
        with open(filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if not status_collection_instance.add_status(row['status_id'],
                                                             row['user_id'], row['status_text']):
                    print('Error: Invalid data in CSV file')
                    return False
        return True
    except FileNotFoundError as error:
        print(f'Error: {error}')
        return False
    except csv.Error as error:
        print(f'CSV Error: {error}')
        return False
    except Exception as error:
        print(f'Unexpected Error: {error}')
        return False


def save_status_updates(filename, status_collection_instance):
    """
    Saves all statuses in status_collection into a CSV file

    Requirements:
    - If there is an existing file, it will overwrite it.
    - Returns False if there are any errors (such as an invalid filename).
    - Otherwise, it returns True.
    """
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['status_id', 'user_id', 'status_text'])
            for status in status_collection_instance.database.values():
                writer.writerow([status.status_id, status.user_id, status.status_text])
        return True
    except FileNotFoundError as error:
        print(f'Error: File not found - {error}')
        return False
    except PermissionError as error:
        print(f'Error: Permission denied - {error}')
        return False
    except csv.Error as error:
        print(f'Error: CSV related error - {error}')
        return False
    except Exception as error:
        print(f'Error: Unexpected error - {error}')
        return False


def add_user(user_id, email, user_first_name, user_last_name, user_collection_instance):
    """
    Creates a new instance of User and stores it in user_collection_instance
    (which is an instance of UserCollection)

    Requirements:
    - user_id cannot already exist in user_collection_instance.
    - Returns False if there are any errors (for example,
    if user_collection_instance.add_user() returns False).
    - Otherwise, it returns True.
    """
    return user_collection_instance.add_user(user_id, email, user_first_name, user_last_name)


def update_user(user_id, email, user_first_name, user_last_name, user_collection_instance):
    """
    Updates the values of an existing user
    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    """
    return user_collection_instance.modify_user(user_id, email, user_first_name, user_last_name)


def delete_user(user_id, user_collection_instance):
    """
    Deletes a user from user_collection_instance.

    Requirements:
    - Returns False if there are any errors (such as user_id not found)
    - Otherwise, it returns True.
    """
    return user_collection_instance.delete_user(user_id)


def search_user(user_id, user_collection_instance):
    """
    Searches for a user in user_collection_instance (which is an instance of UserCollection).

    Requirements:
    - If the user is found, returns the corresponding User instance.
    - Otherwise, it returns None.
    """
    return user_collection_instance.search_user(user_id)
