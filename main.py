# Import functions ******************************
from func.read_token import read_token
from func.exp import *
# Import functions ******************************




# Import modules ********************************
import discord
# Import modules ********************************




# Global definitions ****************************
client = discord.Client()
bot_token = read_token()

exp_data = {}
message_cooldown = {}
# ***********************************************




@client.event
async def on_ready():
    print("Bot is online")
    global exp_data
    exp_data = load_exp_data()


    

@client.event
async def on_message(message):
    
    # If the user is the bot, ignore.
    if message.author == client.user:
        return

    user_id = str(message.author.id)
    
    
    # EXP system on user message *****************************************
    global exp_data
    global message_cooldown

    # Check if the user exists
    if not is_user_in_data(user_id, exp_data):
        exp_data = create_new_user(user_id, exp_data)

    if not is_user_in_data(user_id, message_cooldown):
        message_cooldown = create_new_user_cooldown(user_id, message_cooldown)

        
    # Generate exp for user

    # Check if the user is eligible for exp before giving exp
    TEMP_FLAT_EXP = 10
    if not is_on_exp_gain_cooldown(user_id, message_cooldown):
        exp_data = add_exp(user_id, exp_data, TEMP_FLAT_EXP)
        message_cooldown = set_user_exp_cooldown(user_id, message_cooldown)
    else:
        print("currently on cooldown")


    # Check if sufficient time has passed since last backup.
    if check_backup():
        backup_data(exp_data)
        
    # EXP system on user message *****************************************





# Run the bot.
client.run(bot_token)
