# Import functions ******************************
from func.read_token import read_token
# Import functions ******************************




# Import modules ********************************
import discord

# Import modules ********************************




# Global definitions ****************************
client = discord.Client()
bot_token = read_token()
# ***********************************************




@client.event
async def on_ready():
    print("Bot is online")



    

@client.event
async def on_message(message):

    # If the user is the bot, ignore.
    if message.author == client.user:
        return
    

    # EXP system on user message *****************
    get_user_exp(message.author.id)











# Run the bot.
client.run(bot_token)
