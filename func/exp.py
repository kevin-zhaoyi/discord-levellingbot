import json
from datetime import datetime, timedelta
import dateutil.parser


"""
func check_backup()

Check the last time the data has been backed up.
If the time since last backup has exceeded MINUTES_BEFORE_BACKUP, backup the data.

Input: none

Output: (bool)
    Whether or not the data needs to be backed up.
"""
def check_backup():
    MINUTES_BEFORE_BACKUP = 0.01

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


"""
func backup_data(exp_data)

Backs up the data to the local file.

Input: exp_data                         (dict)
    The experience json data for each user

Output: none
"""

def backup_data(exp_data):
    datafile = open("./data/user_exp_data.json", 'w')
    datafile.write(json.dumps(exp_data))
    datafile.close()

    # Also update the time
    last_backup_time = open("./data/last_called.txt", 'w')
    last_backup_time.write(f"{datetime.now()}")
    last_backup_time.close()




"""
func load_exp_data()

Loads the experience data saved locally to the dynamic memory.

Input: none

Output: exp_data                         (dict)
    The experience json data for each user.
"""
def load_exp_data():
    exp_data_file = open("./data/user_exp_data.json", 'r')
    exp_data = json.loads(exp_data_file.read())
    exp_data_file.close()
    print(exp_data)
    return exp_data




"""
func is_user_in_data(user_id, exp_data)

Queries whether user is in the data.

Input: user_id                     (str)
    The user's id
       data                        (dict)
    The json data dict.

Output: (bool)
    Whether or not the user is in the data.
"""
def is_user_in_data(user_id, data):
    if user_id in data.keys():
        return True
    else:
        return False


    

"""
func create_new_user(user_id, exp_data)

Create a new record for the user in the json data file and sets the exp value to 0.

Input: user_id               (str)
    The user's uid
       exp_data              (dict)
    The data containing all users' exp.

Output: exp_data             (dict)
    The updated data containing all users' exp.
"""
def create_new_user(user_id, exp_data):
    
    exp_data[f"{user_id}"] = 0

    return exp_data




"""
func create_new_user_cooldown(user_id, cooldowns)

Similar to create_new_user(user_id, exp_data), for the cooldown dict.

Input: user_id               (str)
    The user's uid
       cooldowns             (dict)
    The data containing all users' exp gain cooldowns.

Output: cooldowns            (dict)
    The updated data containing all users' exp cooldowns.
"""


def create_new_user_cooldown(user_id, cooldowns):


    cooldowns[f"{user_id}"] = f"{datetime.now()}"

    return cooldowns


"""
func add_exp(user_id, exp_data, amount)

Adds an amount of exp to a user.

Input: user_id                     (str)
    The user's id
       exp_data                    (dict)
    The data containing all users' exp
       amount                      (int)
    An integer amount to add to the user's exp.

Output: exp_data                   (dict)
    The updated data containing all users' exp.
"""
def add_exp(user_id, exp_data, amount):
    user_exp = exp_data[user_id]
    user_exp += amount
    exp_data[user_id] = user_exp
    return exp_data




"""
func time_since_last_exp(user_id, cooldowns)

The time in seconds since the last exp earned by this user.

Input: user_id               (str)
    The user's uid
       cooldowns             (dict)
    The data containing all users' exp gain cooldowns.

Output: total_seconds        (int)
    The number of seconds since the last time the user gained exp.
"""
def time_since_last_exp(user_id, cooldowns):

    last_exp_time = dateutil.parser.parse(cooldowns[user_id])
    time_now = datetime.now()
    
    # The total seconds passed since last backup
    time_delta = (time_now - last_exp_time)
    total_seconds = time_delta.total_seconds()

    return total_seconds






"""
func is_on_exp_gain_cooldown(user_id, cooldowns)

Queries if the user can get exp or not.

Input: user_id               (str)
    The user's uid
       cooldowns             (dict)
    The data containing all users' exp gain cooldowns.

Output: (bool)
    Is the exp gain on cooldown.
"""
def is_on_exp_gain_cooldown(user_id, cooldowns):
    COOLDOWN_TIME_SECS = 10
    
    if time_since_last_exp(user_id, cooldowns) > COOLDOWN_TIME_SECS:
        return False
    else:
        return True




"""
func set_user_exp_cooldown(user_id, cooldowns)

Sets the user's exp gain on cooldown.

Input: user_id               (str)
    The user's uid
       cooldowns             (dict)
    The data containing all users' exp gain cooldowns.

Output: cooldowns            (dict)
    The updated data containing all the exp gain cooldowns.
"""
def set_user_exp_cooldown(user_id, cooldowns):
    cooldowns[user_id] = f"{datetime.now()}"
    return cooldowns
