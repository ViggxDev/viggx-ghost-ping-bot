import discord
from discord.ext import commands

import json
import os

import datetime
from datetime import datetime

import time

token = "ODI2ODA3NTg1MzY1Mjk1MTA1.YGR2kQ.J5Hv55jbkwZBqkfsF2ze2DCOXn0"

client = commands.Bot(command_prefix = '@')

messageSent = False

immune = ["Viggx#6671", "Peja#0243", "jöken#9269", "Deriyxl#1726", "Ghost Ping Remover#7921"] 

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server!')

@client.event
async def on_message(message):
    messageSent = False
    messageAuthor = str(message.author)
    channel = client.get_channel(826858593294221312)
    if messageAuthor != "Ghost Ping Remover#7921":
        for x in immune:
            if str(message.author) == x:
                print(f'{message.author} is immune!')
                await message.author.send(f'{messageAuthor}: {message.content}  -  You are immune to warnings tho!')
                messageSent = True
                if messageAuthor != "Viggx#6671" and messageAuthor != "Ghost Ping Remover#7921":
                    await message.channel.purge(limit=1)
            else:
                if messageSent == False:
                    if message.channel != channel:
                        if "@everyone" in message.content:
                            print(f'{message.author}:{message.content}')
                            #await message.channel.send(f'@Viggx#6671  @{messageAuthor} metioned @.everyone')
                            channel = client.get_channel(826858593294221312)
                            await channel.send(f'{messageAuthor}: {message.content}  -   (SENT IN: #{message.channel})  -   {datetime.now().strftime("%d/%m/%Y - %H:%M:%S")}')
                            await message.author.send(f'Explain yourself: {messageAuthor}: {message.content}  -  {datetime.now().strftime("%d/%m/%Y - %H:%M:%S")}')
                            await message.channel.purge(limit=1)
                            messageSent = True



client.run(token)
