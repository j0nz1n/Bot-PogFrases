import discord
import asyncio
from discord.ext import commands


intents = discord.Intents.all()
client = commands.Bot(command_prefix='&', intents=intents)

@client.command(name='oi')
async def oi(context):
    await context.message.channel.send('Olá, Mundo!')
    
@client.command(name='calc')
async def calculate_expression(context, expression):
    response = eval(expression)
    await context.send('A resposta é: '+ str(response))

@client.event
async def on_ready():
    print('---------------------------------------')
    print('BOT INICIADO!')

client.run('TOKEN DO BOT')