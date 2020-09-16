import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(client.user)
    strings = {'why not both', 'por que no los dos', 'both', 'no los dos', 'por que', 'no los', 'dos', 'los', 'por',
               'que', 'qué', '<@!755731316766670868>'}
    print(message.content)
    msg = message.content.lower()
    for s in strings:
        if s in msg:
            await do_the_thing(message)
            return


async def do_the_thing(message):
    script_dir = os.path.dirname(__file__)
    rel_path = r"porquenolosdos.gif"
    abs_file_path = os.path.join(script_dir, rel_path)
    await message.add_reaction('\U0001F467')
    await message.add_reaction('\U0001F334')
    await message.add_reaction('\U0001F389')
    await message.channel.send('¿Por qué no los dos?', file=discord.File(abs_file_path))
    return


try:
    token = os.environ["DISC_KEY"]
    client.run(token)
except OSError:
    print("Error: Token could not be accessed")
    exit(1)
