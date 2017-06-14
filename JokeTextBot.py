# DAILY REDDIT JOKE BOT
# BY SUNNY NAGAM


import sys, requests, json
from tweetApi import getApi

tweetText = "Daily Reddit Joke:\n"

client = requests.session()
client.headers = {'user-agent':'Python:MyTwitterBot:v0 (by /u/SunnyNagam)'}
client.auth = requests.auth.HTTPBasicAuth('...', '...')

r = client.get(r'https://www.reddit.com/r/Jokes/top/.json')
r.text
data = r.json()

jokeText = ""

for post in data['data']['children']:
	jokeText = post['data']['title'] + "\n"
	jokeText += post['data']['selftext']
	#print jokeText + "\n------------------------"
	if len(jokeText) + len(tweetText) <= 140:
		break

tweetText += jokeText
if len(tweetText) <= 140:
	print tweetText
	api = getApi()
	api.update_status(tweetText)

