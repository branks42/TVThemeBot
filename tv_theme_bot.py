import urllib.request
import urllib.parse
import re
import tweepy, time
import random

# Credentials
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
	# Get songs from text file, put into a list and shuffle them
	list = []
	with open('tv_themes_list.txt') as f:
		list = [x.strip('\n') for x in f.readlines()]
	random.shuffle(list)

	# Loop over playlist
	for theme in list:
		# Get YouTube video id of the first search result
		query_string = urllib.parse.urlencode({"search_query" : theme})
		html_content = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
		search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())

		# Print to console
		print("[" + time.ctime() + "] Theme tweeted: " + theme + "\nhttp://www.youtube.com/watch?v=" + search_results[0])

		# Tweet the song
		api.update_status(theme + "\n#TVThemeMachine" + "\n" + "https://www.youtube.com/watch?v=" + search_results[0])

		# Rerun script every 24 hrs
		time.sleep(86400)
