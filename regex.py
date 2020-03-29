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