from peewee import *

# Define the database file name
DATABASE_NAME = 'socialnetwork.db'

# Create a SQLite database instance
database = SqliteDatabase(DATABASE_NAME)

# Define the base model for all tables
class BaseModel(Model):
    class Meta:
        database = database

# Define the Users table
class Users(BaseModel):
    user_id = CharField(primary_key=True, max_length=30)
    user_name = CharField(max_length=30)
    user_last_name = CharField(max_length=100)
    user_email = CharField()

# Define the Status table
class Status(BaseModel):
    status_id = AutoField(primary_key=True)
    user_id = ForeignKeyField(Users, backref='status_updates', on_delete='CASCADE')
    status_text = TextField()

# Connect to the database and create tables
def create_tables():
    with database:
        database.create_tables([Users, Status])

# Run this function to create the tables when the script is executed
if __name__ == '__main__':
    create_tables()
