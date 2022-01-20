# Import functions ******************************
from func.read_token import read_token
# Import functions ******************************



import discord



# Global definitions ****************************
client = discord.Client()
bot_token = read_token()
# ***********************************************




@client.event
async def on_ready():
    print("Bot is online")



    

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$hello"):
        await message.channel.send("Hello")

client.run(bot_token)
