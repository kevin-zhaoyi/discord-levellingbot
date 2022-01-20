import json
from datetime import datetime, timedelta
import dateutil.parser


"""
def check_backup()

Check the last time the data has been backed up.
If the time since last backup has exceeded MINUTES_BEFORE_BACKUP, backup the data.

Input: none

Output: (bool)
    Whether or not the data needs to be backed up.
"""
    
def check_backup():
    MINUTES_BEFORE_BACKUP = 15

    last_backup_time = open("./data/last_called.txt", 'r')
    backup_time = last_backup_time.read()
    last_backup_time.close()

    backup_time_datetime = dateutil.parser.parse(backup_time)
    current_time = datetime.now()

    # The total minutes passed since last backup
    time_delta = (current_time - backup_time_datetime)
    total_minutes = time_delta.total_seconds() / 60

    # Check if a new backup is required
    if total_minutes > MINUTES_BEFORE_BACKUP:
        return True
    else:
        return False

    
def backup_data(exp_data):
    datafile = open("./data/user_exp_data.json", 'w')
    datafile.write(json.dumps(exp_data))
    datafile.close()

    # Also update the time
    last_backup_time = open("./data/last_called.txt", 'w')
    last_backup_time.write(f"{datetime.now()}")
    last_backup_time.close()


def load_exp_data():
    exp_data_file = open("./data/user_exp_data.json", 'r')
    exp_data = json.loads(exp_data_file.read())
    exp_data_file.close()
    return exp_data

def is_user_in_data(user_id, exp_data):
    if user_id in exp_data.keys():
        return True
    else:
        return False

"""
def create_new_user(user_id)

Create a new record for the user in the json data file and sets the exp value to 0.

Input: user_id               (int)
    The user's uid
       exp_data              (dict)
    The data containing all users' exp.

Output: exp_data             (dict)
    The updated data containing all users' exp.
"""
def create_new_user(user_id, exp_data):

    # Create new json record
    new_user = {f"{user_id}": 0}

    # Append json record.
    exp_data.update(new_user)

    return exp_data






    
