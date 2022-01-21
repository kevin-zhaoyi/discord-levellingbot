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
level_data = {}
message_cooldown = {}
level_requirements = {}

bot = discord.ext.commands.Bot
# ***********************************************




@client.event
async def on_ready():
    print("Bot is online")
    global exp_data
    global level_data
    global level_requirements
    exp_data = load_exp_data()
    level_data = load_level_data()
    level_requirements = load_level_requirements()
    

@client.event
async def on_message(message):
    
    # If the user is the bot, ignore.
    if message.author == client.user:
        return

    user_id = str(message.author.id)
    
    
    # EXP system on user message *****************************************
    global exp_data
    global level_data
    global level_requirements
    global message_cooldown

    # Check if the user exists
    if not is_user_in_data(user_id, exp_data):
        exp_data = create_new_user(user_id, exp_data)

    if not is_user_in_data(user_id, level_data):
        level_data = create_new_user(user_id, level_data)
    
    if not is_user_in_data(user_id, message_cooldown):
        message_cooldown = create_new_user_cooldown(user_id, message_cooldown)

        

    # Check if the user is eligible for exp before giving exp
    if not is_on_exp_gain_cooldown(user_id, message_cooldown):
        JACKPOT_EXP = 1000
        
        exp_data = add_exp(user_id, exp_data, randomise_exp())

        # Random chance to get lots of exp
        if lottery_exp():
            exp_data = add_exp(user_id, exp_data, JACKPOT_EXP)
            
        message_cooldown = set_user_exp_cooldown(user_id, message_cooldown)

    # Check if the user is eligible for level up
    if can_level_up(user_id, exp_data, level_data, level_requirements):
        exp_data, level_data, level_requirements = level_up(user_id, exp_data, level_data, level_requirements)
        await message.channel.send(f"Congratulations, you levelled up to level {level_data[user_id]}!")

    # Check if sufficient time has passed since last backup.
    if check_backup():
        backup_data(exp_data, level_data)
        
    # EXP system on user message *****************************************



    
    await client.process_commands(message)


@client.command()
async def level(ctx):
    global exp_data
    global level_data
    global level_requirements

    user_id = str(ctx.message.author.id)
    user_exp = exp_data[user_id]
    user_level = level_data[user_id]
    
    user_id = str(ctx.message.author.id)
    await ctx.send(f"You have {user_exp}/{level_requirements[str(user_level+1)]} exp. You need {level_requirements[str(user_level+1)]-user_exp} more exp until level {user_level+1}.")



# Run the bot.
client.run(bot_token)
