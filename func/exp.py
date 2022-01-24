import json
from datetime import datetime, timedelta
import dateutil.parser
import random

"""
func check_backup()

Check the last time the data has been backed up.
If the time since last backup has exceeded MINUTES_BEFORE_BACKUP, backup the data.

Input: none

Output: (bool)
    Whether or not the data needs to be backed up.
"""
def check_backup():
    MINUTES_BEFORE_BACKUP = 10

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
       level_data                       (dict)
    The level json data for each user

Output: none
"""

def backup_data(exp_data, level_data):
    datafile = open("./data/user_exp_data.json", 'w')
    datafile.write(json.dumps(exp_data))
    datafile.close()

    datafile = open("./data/user_level_data.json", 'w')
    datafile.write(json.dumps(level_data))
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
    return exp_data

def load_level_data():
    level_data_file = open("./data/user_level_data.json", 'r')
    level_data = json.loads(level_data_file.read())
    level_data_file.close()
    return level_data

def load_level_requirements():
    level_requirements_file = open("./data/level_requirements.json", 'r')
    level_requirements = json.loads(level_requirements_file.read())
    level_requirements_file.close()
    return level_requirements


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
    print(exp_data)
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


def randomise_exp():
    return random.randint(1,50)

def lottery_exp():
    if random.randint(1,100) == 77:
        return True
    else:
        return False

def calculate_new_level_requirement(level):
    """ Formula for the exp needed per level
        lv^3 * 1000exp.
    """
    return pow(level, 3) * 1000

def level_up(user_id, exp_data, level_data, level_requirements):
    
    user_level = level_data[user_id]
    user_exp = exp_data[user_id]

    #user_exp = user_exp - level_requirements[str(user_level + 1)]
    user_level = user_level + 1

    exp_data[user_id] = user_exp
    level_data[user_id] = user_level

    
    # Check there is a requirement for next level.
    if not str(user_level + 1) in level_requirements.keys():
        level_requirements[str(user_level + 1)] = calculate_new_level_requirement(user_level + 1)
        # Write to local file
        datafile = open("./data/level_requirements.json", 'w')
        datafile.write(json.dumps(level_requirements))
        datafile.close()
    return (exp_data, level_data, level_requirements)

def can_level_up(user_id, exp_data, level_data, level_requirements):

    user_level = level_data[user_id]
    user_exp = exp_data[user_id]
    print(str(user_level + 1))
    print(level_requirements.keys())
    if user_exp >= level_requirements[str(user_level + 1)]:
        return True
    else:
        return False
    
