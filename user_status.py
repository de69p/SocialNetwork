import logging

logging.basicConfig(filename='log_07_20_2023.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UserStatus:
    """
    class to hold status message data
    """
    def __init__(self, status_id, user_id, status_text):
        self.status_id = status_id
        self.user_id = user_id
        self.status_text = status_text

class UserStatusCollection:
    """
    Collection of UserStatus messages
    """

    def __init__(self):
        self.database = {}

    def add_status(self, status_id, user_id, status_text):
        """
        add a new status message to the collection
        """
        if status_id in self.database:
            logging.error(
                f"An error occurred while trying to add a new status with ID '{status_id}'. Status ID already exists.")
            # Rejects new status if status_id already exists
            return False
        new_status = UserStatus(status_id, user_id, status_text)
        self.database[status_id] = new_status
        logging.info(f"New status with ID '{status_id}' added successfully.")
        return True

    def modify_status(self, status_id, user_id, status_text):
        """
        Modifies a status message

        The new user_id and status_text are assigned to the existing message
        """
        if status_id not in self.database:
            # Rejects update if the status_id does not exist
            logging.error(
                f"An error occurred while trying to modify status with ID '{status_id}'. Status ID does not exist.")
            return False

        self.database[status_id].user_id = user_id
        self.database[status_id].status_text = status_text
        logging.info(f"Status with ID '{status_id}' modified successfully.")
        return True

    def delete_status(self, status_id):
        """
        deletes the status message with id, status_id
        """
        if status_id not in self.database:
            # Fails if status does not exist
            logging.error(
                f"An error occurred while trying to delete status with ID '{status_id}'. Status ID does not exist.")
            return False
        del self.database[status_id]
        logging.info(f"Status with ID '{status_id}' deleted successfully.")
        return True

    def search_status(self, status_id):
        """
        Find and return a status message by its status_id

        Returns an empty UserStatus object if status_id does not exist
        """
        if status_id not in self.database:
            logging.error(f"Status with ID '{status_id}' not found during the search.")
            return UserStatus(None, None, None)

        logging.info(f"Status with ID '{status_id}' found during the search.")
        return self.database[status_id]

