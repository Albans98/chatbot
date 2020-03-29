"""#**Discord**

[Reference](https://discordpy.readthedocs.io/en/latest/api.html#event-reference)
[API Reference](https://discordpy.readthedocs.io/en/latest/api.html)

[Channel](https://discordapp.com/channels/691996782057619456/691996782057619459)
[discord dev](https://discordapp.com/developers/applications/691997857015791636/bo)
"""


import discord 

TOKEN = 'NjkxOTk3ODU3MDE1NzkxNjM2.XnoJaQ.473ufnNjntorB2UO45igtbNXp3M'
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))

        elif message.content.startswith('!yo'):
            await message.channel.send('Yo t you to')

client = MyClient()
client.run(TOKEN)

from discord.ext.commands import Bot
import random
BOT_PREFIX = ("?", "!")
TOKEN = "NjkxOTk3ODU3MDE1NzkxNjM2.XnoJaQ.473ufnNjntorB2UO45igtbNXp3M"  # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix=BOT_PREFIX)
@client.command()
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await context.send(random.choice(possible_responses) + ", " + context.message.author.mention) 
client.run(TOKEN)

import discord 

TOKEN = 'NjkxOTk3ODU3MDE1NzkxNjM2.XnoJaQ.473ufnNjntorB2UO45igtbNXp3M'
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        await message.channel.send(message.content)
        print(message.content)

client = MyClient()
client.run(TOKEN)

print("Testttt")