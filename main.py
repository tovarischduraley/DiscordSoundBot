import asyncio
import discord
from discord.ext import commands
import keyboard
from config import config

TOKEN = config['TOKEN']
PATH = config['SOUND_PATH']
client = commands.Bot('.')


@client.event
async def on_ready():
    print('Bot is ready')


def play_sound(vc, name):
    try:
        vc.play(discord.FFmpegPCMAudio(PATH + name))
    except Exception as e:
        print(e)
        pass


@client.command(pass_contecxt=False)
async def join(ctx, amount=1):
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio(PATH + 'HELLO THERE.mp3'))
    await ctx.channel.purge(limit=amount)

    while True:
        try:
            if keyboard.is_pressed('up'):
                play_sound(vc, 'VI KA.mp3')
                await asyncio.sleep(0.2)
            if keyboard.is_pressed('down'):
                play_sound(vc, 'BRUH.mp3')
                await asyncio.sleep(0.2)
            if keyboard.is_pressed('right'):
                play_sound(vc, 'HE FUCKED UP.mp3')
                await asyncio.sleep(0.2)
            if keyboard.is_pressed('left'):
                play_sound(vc, 'directedby.mp3')
                await asyncio.sleep(0.2)

            if keyboard.is_pressed('0'):
                vc.stop()
                await asyncio.sleep(0.2)
            else:
                await asyncio.sleep(0.1)
        except Exception as ex:
            return print(str(ex))


@client.command()
async def leave(ctx, amount=1):
    await ctx.voice_client.disconnect()
    await ctx.channel.purge(limit=amount)


@client.command()
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)


if __name__ == '__main__':
    client.run(TOKEN)
