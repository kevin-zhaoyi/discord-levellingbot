import discord

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is online")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$hello"):
        await message.channel.send("Hello")

client.run("ODE1MTg3MDIzNTI1NTc2NzA0.YDowEw.rNogUwEn1zSI6bvy9cWpuWmtPgg")
