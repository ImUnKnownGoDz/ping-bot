import discord
import sys

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
   print("Your bot is ready")
   await client.change_presence(activity=discord.Game(name='https://github.com/ImUnKnownGoDz/ping-bot'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "start":
        while 1 == 1:
            await message.channel.send("@everyone")



client.run("your token")
