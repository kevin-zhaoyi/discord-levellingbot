import json



def load_exp_data():
    exp_data_file = open("./data/user_exp_data.json", 'r')
    exp_data = json.load(exp_data_file)
    exp_data_file.close()
    return exp_data


"""
def create_new_user(user_id)

Create a new record for the user in the json data file and sets the exp value to 0.

Input: user_id               (int)
    The user's uid

Output: none
"""
def create_new_user(user_id):

    # Create new json record
    new_user = {f"{user_id}": 0}

    # Append json record.




"""
func get_user_exp(user_id)

Gets the user's current experience points.

Input: user_id               (int)
    The user's uid.
    
Output: user_exp             (int)
    The user's current exp level.
"""
def get_user_exp(user_id):

    exp_data_file = open("./data/user_exp_data.json", 'r')
    exp_data = json.load(exp_data_file)
    exp_data_file.close()

    # If user does not exist, make record for user and set exp to 0.
    if not user_id in exp_data.keys():
        create_new_user(user_id)


    user_exp = exp_data[user_id]
    
    return user_exp


    
