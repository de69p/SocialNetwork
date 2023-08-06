import logging
from peewee import *
from socialnetwork_model import Users
from socialnetwork_model import Status


# Configure the logging module
logging.basicConfig(filename='log_07_20_2023.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class UserCollection:
    def add_user(self, user_id, user_name, user_last_name, user_email):
        try:
            Users.create(
                user_id=user_id,
                user_name=user_name,
                user_last_name=user_last_name,
                user_email=user_email
            )
            logging.info(f"New user with ID '{user_id}' added successfully.")
            return True
        except IntegrityError:
            logging.error(f"An error occurred while trying to add a new user with ID '{user_id}'. User already exists.")
            return False

    def delete_user(self, user_id):
        try:
            user = Users.get(Users.user_id == user_id)
            user.delete_instance()
            logging.info(f"User with ID '{user_id}' deleted successfully.")
            return True
        except DoesNotExist:
            logging.error(f"An error occurred while trying to delete user with ID '{user_id}'. User does not exist.")
            return False

    def search_user(self, user_id):
        try:
            user = Users.get(Users.user_id == user_id)
            return {
                'user_id': user.user_id,
                'user_name': user.user_name,
                'user_last_name': user.user_last_name,
                'user_email': user.user_email
            }
        except DoesNotExist:
            return None

class UserStatusCollection:
    def add_status_update(self, user_id, status_text):
        try:
            user = Users.get(Users.user_id == user_id)
            Status.create(user_id=user, status_text=status_text)
            logging.info(f"New status update added for user with ID '{user_id}'.")
            return True
        except DoesNotExist:
            logging.error(f"An error occurred while trying to add a new status update. User with ID '{user_id}' does not exist.")
            return False

    def delete_status_update(self, status_id):
        try:
            status = Status.get(Status.status_id == status_id)
            status.delete_instance()
            logging.info(f"Status update with ID '{status_id}' deleted successfully.")
            return True
        except DoesNotExist:
            logging.error(f"An error occurred while trying to delete status update with ID '{status_id}'. Status update does not exist.")
            return False

    def search_status_update(self, status_id):
        try:
            status = Status.get(Status.status_id == status_id)
            return {
                'status_id': status.status_id,
                'user_id': status.user_id.user_id,
                'status_text': status.status_text
            }
        except DoesNotExist:
            return None
