import discord

client = discord.Client()

# Hide token from being comitted
tokenfile = open("token.txt", 'r')
token = tokenfile.read()
tokenfile.close()

@client.event
async def on_ready():
    print("Bot is online")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$hello"):
        await message.channel.send("Hello")

client.run(token)
