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