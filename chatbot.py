# -*- coding: utf-8 -*-

# **Test RE**


import re

# Equivalence au flag "g" (global) : re.findall
test = re.findall('chatbot|regex', 'Hey, je suis un chatbot ! Les regex je les trouve géniales !')
print(test)

# Commencer au tout début du string : re.match
test = re.match('.*chatbot', 'Hey, je suis un chatbot ! Les regex je les trouve géniales !')
# Il faut utiliser .group pour récupérer les valeurs
if test:
  print(test.group())

# Pour trouver le premier élément qui match : re.search
test = re.search('chatbot|regex', 'Hey, je suis un chatbot ! Les regex je les trouve géniales !')
if test:
  print(test.group())

# Utilisation des flags dans les paramètres
"""
re.I	re.IGNORECASE	: ignore case.
re.M	re.MULTILINE : make begin/end {^, $} consider each line.
re.S	re.DOTALL : make . match newline too.
re.U	re.UNICODE : make {\w, \W, \b, \B} follow Unicode rules.
re.L	re.LOCALE : make {\w, \W, \b, \B} follow locale.
re.X	re.VERBOSE : allow comment in regex.
"""

test = re.findall('cHatBoT|REgeX', 'Hey, je suis un chatbot ! Les regex je les trouve géniales !', re.I)
print(test)

"""# **Test Chatbot**"""

QuestionsFine=["how are you?", "whats'up"]
import string
flag=True
print("BOT: Hi! I am a GROOT the Gift Finder ChatBot")
print("User :", end="")
user_response = input()
user_response=user_response.lower()
if user_response in QuestionsFine : print("BOT: Fine and you?")
print("User :", end="")
user_response = input()
print("BOT: How can I help you ?")
while(flag==True):
    print("User :", end="")
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("BOT: You are welcome..")
            print("BOT: Bye! see you soon")
        else:
            print("BOT: test")
            """
            if(greeting(user_response)!=None):
                print("BOT: "+greeting(user_response) +"! I a movie recommender chatbot, I am here to help you in your movie selection. Would you like tot try? If you want to exit, type Bye!")
            else:
                print("BOT: ",end="")
                
                print(response(user_response, current_movie, userInput))
                #sent_tokens.remove(user_response)"""
    else:
        flag=False
        print("BOT: Bye! Take care..")

"""#**Discord**

[Reference](https://discordpy.readthedocs.io/en/latest/api.html#event-reference)
[API Reference](https://discordpy.readthedocs.io/en/latest/api.html)

[Channel](https://discordapp.com/channels/691996782057619456/691996782057619459)
[discord dev](https://discordapp.com/developers/applications/691997857015791636/bo)
"""

pip install discord.py

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

"""# **API TEST**

[pour tester](https://gurujsonrpc.appspot.com/)

[web api](https://jooble.org/api/about)
"""

import http.client

host = 'jooble.org'
key = '824f5d8e-312e-44a9-add7-17ab2b9519c7'

connection = http.client.HTTPSConnection(host)
#request headers
headers = {"Content-type": "application/json"}
#json query
#body = '{ "keywords": "it", "location": "Bern"}'
body = '{"keywords": "manager", "location": "Paris", "radius": "50","salary": "2000" }'
connection.request('POST','/api/' + key, body, headers)
response = connection.getresponse()
#print(response.read().decode())

import json

# Decode UTF-8 bytes to Unicode, and convert single quotes 
# to double quotes to make it valid JSON
my_json = response.read().decode()
print(my_json)
print("--"*20)

data = json.loads(my_json)
s = json.dumps(data, indent=4, sort_keys=True)
print(s)

"""# **Fuction Chatbot**

* entree :: message
* sortie :: strindg reponse 

[Joke API](https://github.com/15Dkatz/official_joke_api)

[ALL API](https://github.com/public-apis/public-apis/blob/master/README.md)

[tuto IA](https://github.com/DevDungeon/Cathy/blob/master/cathy/cathy.py)
"""

import numpy as np
import random
import string # to process standard python strings

print("\U0001F44C")

#https://unicode.org/emoji/charts/full-emoji-list.html
GREETING_INPUTS = ("hello", "hi", "greetings","yo","hey",)
ASKINGHOW=("how are you", "sup", "what's up")
GREETING_RESPONSES = ["Hi! \U0001F44B", "Hey", "Bonjour \N{grinning face} ", "Hello!"]
YES=("yes", "sure", "ok \U0001F44C", "okay", "another",)

# Checking for greetings
def greeting(message):
    """If user's input is only a greeting, return a greeting response plus a presentation
    If user's input is a greeting and asking how are , return a greeting response plus a fine answer
    """
    msgRep=""
    res1= False 
    for word in message.split():#.content.split():
        if word.lower() in GREETING_INPUTS:## a remplacer par des regex
          res1 = True
    if res1 == True :
      msgRep = random.choice(GREETING_RESPONSES)
    res2 = False 
    for word in message.split():#.content.split():
      if word.lower() in ASKINGHOW:## a remplacer par des regex
        res2 = True
          
    if res1 == False and res2==False :
      return

    if res2 == True : msgRep = msgRep + "\nI am fine , Thx for asking"
    else : msgRep = msgRep+"\nI am Groot!, Nice to meet you"##,{0.author.mention}".format(message)
    msgRep = msgRep+"\nHow can I help you today ?"
    return msgRep

print(greeting("hi , sup"))

