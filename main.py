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
# ***********************************************




@client.event
async def on_ready():
    print("Bot is online")
    exp_data = load_exp_data()


    

@client.event
async def on_message(message):
    
    # If the user is the bot, ignore.
    if message.author == client.user:
        return

    user_id = str(message.author.id)
    global exp_data
    
    
    # EXP system on user message *****************
    if not is_user_in_data(user_id, exp_data):
        exp_data = create_new_user(user_id, exp_data)

    # Generate exp for user
    TEMP_FLAT_EXP = 10
    add_exp(user_id, exp_data, TEMP_FLAT_EXP)



    # Check if 15 minutes has passed since last backup.
    if check_backup():
        backup_data(exp_data)
        






# Run the bot.
client.run(bot_token)
