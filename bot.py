import discord 
from discord.ext import commands
from response import *
import os
from main import configure


configure()

async def send_message(message, user_message, is_private):
    try :
        response = handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
        
def run_discord_bot():
    intent = discord.Intents.default()
    intent.message_content = True
    client = discord.Client(intents=intent)
    
    bot = commands.Bot(command_prefix="!", intents=intent)
    
    # sclient = commands.Bot(command_prefix="-", intents=intent)
    # slash = SlashCommand(sclient)

    # @slash.slash(name="hello")
    # async def ping(res):
    #     await res.send("Hello back fro slash commands")
    
    @client.event
    async def on_ready():
        print(f"{client.user} is now running!")
    
    @bot.event
    async def on_ready():
        print("Bot is now running!")
        try:
            synced = await bot.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(f"Error : {e}")
    
    @bot.tree.command(name="hello")
    async def hello(interaction: discord.Integration):
        await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a slash command",ephemeral=True)
        
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        print(message.content)
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f"{username} said: {user_message} ({channel})")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else :
            await send_message(message, user_message, is_private=False)
            
        
    client.run(os.environ['TOKEN'])