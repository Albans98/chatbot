# ------------------------------------------------------------------------------------------------------------------------------

# Import packages

import re
import nltk
import http.client
import json
import random
import requests
import string
import discord

# -----  Comment this line if you already have 'wordnet' installed -----
nltk.download('wordnet')

from nltk.corpus import wordnet

# Patterns --------------------------------------

def get_synonyms(word):
	data = wordnet.synsets(word)
	synonyms = []
	for i in data:
		for j in i.lemmas():
			synonyms.append(str(j.name()))
	return set(synonyms)


# Create basic patterns
basic_patterns = []

GREETING_INPUTS = get_synonyms('Hello')
GREETING_INPUTS = '+|'.join(GREETING_INPUTS)
GREETING_OUTPUTS = ["Hi ! \U0001F44B", "Hello \N{grinning face}"]
p1 = {"pattern": GREETING_INPUTS, "intent": GREETING_OUTPUTS}
basic_patterns.append(p1)

THANKS_INPUTS = get_synonyms('thank')
THANKS_INPUTS = '+|'.join(THANKS_INPUTS)
THANKS_INPUTS += '+'
THANKS_OUTPUTS = ["You're welcome ! \U0001F44B", "Be my guest ! \U0001F44B"]
p2 = {"pattern": THANKS_INPUTS, "intent": THANKS_OUTPUTS}
basic_patterns.append(p2)

ASKING_HOW_INPUTS = get_synonyms('okay')
ASKING_HOW_INPUTS = "+|".join(ASKING_HOW_INPUTS)
ASKING_HOW_INPUTS += "+|how.*you+"
ASKING_HOW_INPUTS += "|what's up+"
ASKING_HOW_OUTPUTS = ["I am happy to be with you ! \U0001F44B", "I am a happy Groot ! \U0001F44B"]
p3 = {"pattern": ASKING_HOW_INPUTS, "intent": ASKING_HOW_OUTPUTS}
basic_patterns.append(p3)

HELP_INPUTS = get_synonyms('Help')
HELP_INPUTS = '+|'.join(HELP_INPUTS)
help_string = "Groot JobSeeker is a chatbot, here to help you find a job ! & can also tell you a funny joke :D\n it can respond to five types of conversation :"
help_string += "\nGreeting  ⇒ hi, hello, what's up ? ..."
help_string += "\nBye ⇒ bye, goodbye, see you ..."
help_string += "\nJoking ⇒  tell me a joke, let's laugh ..."
help_string += "\nHelping  ⇒  help please ..."
help_string += "\nJob ⇒  I am looking for a job, find me an intership ...\n"
HELP_OUTPUTS = help_string
p4 = {"pattern": HELP_INPUTS, "intent": HELP_OUTPUTS}
basic_patterns.append(p4)

BYE_INPUTS = get_synonyms('Bye')
BYE_INPUTS = '+|'.join(BYE_INPUTS)
BYE_OUTPUTS = ["Bye !", "Goodbye !", "See you soon !", "Have a nice day !"]
p5 = {"pattern": BYE_INPUTS, "intent": BYE_OUTPUTS}
basic_patterns.append(p5)

JOKE_INPUTS = get_synonyms('joke')
JOKE_INPUTS = '+|'.join(JOKE_INPUTS)
JOKE_OUTPUTS = ""
p6 = {"pattern": JOKE_INPUTS, "intent": JOKE_OUTPUTS}
basic_patterns.append(p6)


# Create patterns for advanced function
JOB_INPUTS = get_synonyms('job')
JOB_INPUTS.add('intern')
JOB_INPUTS.add('trainee')
JOB_INPUTS = '+|'.join(JOB_INPUTS)

IDC_INPUTS = get_synonyms('care')
IDC_INPUTS.add('whatever')
IDC_INPUTS = '+|'.join(IDC_INPUTS)
IDC_CITIES = ['Paris', 'Seoul', 'San Francisco', 'Seattle', 'Sydney', 'Madrid', 'London', 'New York', 'Morocco', 'New Dehli']
IDC_SALARY = ['10', '100', '1000', '10000', '20', '200', '2000', '20000']

# Simple chatbot functionalities --------------------------------------

def joking():
  msgRep = ""
  msgRep = msgRep+"Let me tell you a Joke\n"
  APIJoke = 'https://official-joke-api.appspot.com/random_joke'
  r = requests.get(APIJoke)
  resJson = r.json()
  msgRep = msgRep + resJson["setup"]
  msgRep = msgRep + "\n.....\n"
  msgRep = msgRep + resJson["punchline"] + "\n"
  msgRep = msgRep + "\U0001F923 \U0001F923 \U0001F923 \U0001F923"
  return msgRep

# This function is default function, when no entities were found
def get_default():
	response = "I am Groot ?! \U0001F914.\nPlease try again or write 'Help'."
	return response


# This function only catch entities for "easy" questions stored in our basic_patterns dictionary (Hello, Goodbye, Help, Jokes)
def get_simple_response(msg, author):
	for item in basic_patterns:
		global status
		global values
		global data
		entity = re.findall(item['pattern'], msg, re.I)
		if entity:
			if item['intent']:
				if (item['pattern'] == BYE_INPUTS):
					if status > 0:
						status = 0
						values = []
						data = []
						return "Sorry to hear that you leave now \n" + random.choice(item['intent']) + " " + author
				if (item['pattern'] == GREETING_INPUTS) or (item['pattern'] == BYE_INPUTS):
					return random.choice(item['intent']) + " " + author
				if item['pattern'] == HELP_INPUTS:
					return item['intent']
				else:
					return random.choice(item['intent'])
			else:
				return joking()
	return ""




# Job chatbot functionality --------------------------------------


def get_jobtitle(msg):
	return ["Got it !", msg]


def get_location(msg):
	regex = "in ([a-z])+( [a-z]+)?"
	match = re.search(regex, msg, re.I)
	if match:
		match = match.group().split("in ")
		return ["Got it !", match[1]]
	elif re.findall(IDC_INPUTS, msg, re.I):
		return ["Got it !", random.choice(IDC_CITIES)]
	elif len(msg.split()) <= 2:
		return ["Got it !", msg]
	return ["Hey, I'm sorry but I couldn't get what you said \U0001F501.\nCan you try 'I want a job in Paris !' for example ?", msg]

def get_salary(msg):
	regex = "[0-9]+"
	match = re.search(regex, msg)
	if match:
		return ["Got it !", str(match.group())]
	elif re.findall(IDC_INPUTS, msg, re.I):
		return ["Got it !", random.choice(IDC_SALARY)]
	return ["Hey, I'm sorry but I couldn't get what you said \U0001F501.\nCan you try '10' for example ?", msg]

def get_max(msg):
	regex = "[0-9]+"
	match = re.search(regex, msg)
	if match:
		if (int(match.group()) < 1) or (int(match.group()) > 3):
			return ["Got it !", "3"]
		return ["Got it !", str(match.group())]
	return ["Hey, I'm sorry but I couldn't get what you said \U0001F501.\nCan you try '1' for example ?", msg]

def check_job(msg, status):
	if status > 0:
		return True
	else:
		entity = re.findall(JOB_INPUTS, msg, re.I)
		if entity:
			return True
	return False

def get_job_response(status, msg):
	if(status == 1):
		return get_jobtitle(msg)
	if(status == 2):
		return get_location(msg)
	if(status == 3):
		return get_salary(msg)
	if(status == 4):
		return get_max(msg)

def display_job(values, start):
	name = values[0]
	location = values[1]
	salary = values[2]
	body = '{"keywords": "'+ str(name) + '", "location": "' + str(location) + '", "radius": "50", "salary": "' + str(salary) + '"}'
	host = 'jooble.org'
	key = '824f5d8e-312e-44a9-add7-17ab2b9519c7'
	connection = http.client.HTTPSConnection(host)
	headers = {"Content-type": "application/json"}
	connection.request('POST','/api/' + key, body, headers)
	response = connection.getresponse()
	my_json = response.read().decode()
	data = json.loads(my_json)
	jobs = ""
	for i in range(start, len(data['jobs'])):
		if i < int(values[3]):
			jobs += "Job title: " + str(data['jobs'][i]['title'])
			jobs += "\nJob location: " + str(data['jobs'][i]['location'])
			jobs += "\nJob link: " + str(data['jobs'][i]['link'])
			jobs += "\nJob description: " + str(data['jobs'][i]['snippet'])
			jobs += "\n\n"
	if jobs == "":
		jobs = "I didn't find any job for the search criteria.\n"
	return [jobs, data]





# Main -------------------------------------------

def chatbot(msg, author):
	global status
	global values
	global data
	response = get_simple_response(msg, author)
	if check_job(msg, status):
		if status > 0 and status < 6:
			job_res = get_job_response(status, msg)
			if job_res[0] == "Got it !":
				values.append(job_res[1])
				status += 1
			response += "\n" + job_res[0]
			if status == 2:
				response += "\nWhere do you want this Job ? \U0001F5FA"
			if status == 3:
				response += "\nHow much do you want to earn for this Job ? \U0001F4B0"
			if status == 4:
				response += "\nHow many jobs do you want to display (max 3) ?"
		if status == 0:
			response += "\nLet's find your dream job ! I will ask you some questions first."
			response += "\nWhat is the name of your desired position ? \U0001F50F"
			status += 1
		if status == 6:
			if re.findall('yes+|ok+', msg, re.I):
				values[3] = "6"
				jobs = display_job(values, 3)[0]
				response += "\n" + jobs
			else:
				response += "\nOkay, no more !\n"
			data = []
			values = []
			status = 0
		if status == 5:
			jobs = display_job(values, 0)
			data = jobs[1]
			jobs = jobs[0]
			response += "\n" + jobs
			if int(values[3]) <= len(data['jobs']):
				response += "\n\n I have more results ! Do you want to see more ?\n"
			status += 1
	if response == "":
		response = get_default()
	return response

status = 0
values = []
data = []


TOKEN = ''
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
        await message.channel.send(chatbot(message.content, '{0.author.mention}'.format(message)))

client = MyClient()
client.run(TOKEN)