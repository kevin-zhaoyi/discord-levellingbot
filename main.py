# Import functions ******************************
from func.read_token import read_token
from func.exp import *
# Import functions ******************************




# Import modules ********************************
import discord
from discord.ext import commands
# Import modules ********************************




# Global definitions ****************************
intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)
bot_token = read_token()

exp_data = {}
message_cooldown = {}

bot = discord.ext.commands.Bot
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

        

    # Check if the user is eligible for exp before giving exp
    TEMP_FLAT_EXP = 10
    if not is_on_exp_gain_cooldown(user_id, message_cooldown):
        print('s')
        exp_data = add_exp(user_id, exp_data, TEMP_FLAT_EXP)
        message_cooldown = set_user_exp_cooldown(user_id, message_cooldown)


    # Check if sufficient time has passed since last backup.
    if check_backup():
        backup_data(exp_data)
        
    # EXP system on user message *****************************************



    
    await client.process_commands(message)


@client.command()
async def level(ctx):
    global exp_data
    user_id = str(ctx.message.author.id)
    await ctx.send(f"You have {exp_data[user_id]} exp.")



# Run the bot.
client.run(bot_token)
