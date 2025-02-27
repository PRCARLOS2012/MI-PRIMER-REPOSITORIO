import discord
from discord.ext import commands
from bot_logic import gen_pass

#La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
#Activar el privilegio de lectura de mensajes
intents.message_content = True
#Crear un bot en la variable cliente y transferirle los privilegios

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! {bot.user}!')

@bot.command()
async def bye(ctx):
    await ctx.send(f'\U0001f642 {bot.user}!')

@bot.command()
async def password(ctx):
    await ctx.send(f'{gen_pass(10)} {bot.user}!')

@bot.command()
async def Help(ctx):
    await ctx.send(f'Lista de comandos {bot.user}!')

@bot.command()
async def repeat(ctx, times = 10, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

#Token:
bot.run("")