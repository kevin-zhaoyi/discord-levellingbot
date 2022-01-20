# Import functions ******************************
from func.read_token import read_token
from func.exp import *
# Import functions ******************************




# Import modules ********************************
import discord
from datetime import datetime, timedelta
import time
import dateutil.parser
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

    

    
    
    # EXP system on user message *****************
    get_user_exp(message.author.id)



    # Check if 15 minutes has passed since last backup.
    if(check_backup()):
        datafile = open("./data/user_exp_data.json", 'r')
        backup_data(datafile, data)
        datafile.close()






# Run the bot.
client.run(bot_token)
