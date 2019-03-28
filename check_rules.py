#Are NYC parking rules suspended today? How about tomorrow?

import requests, re, datetime

#Get {MONTH DAY}-format date strings. These will be used to compare against later
#Ex: "March 12"
today = '{:%B %d}'.format(datetime.datetime.today())
tomorrow = '{:%B %d}'.format(datetime.date.today() + datetime.timedelta(days=1))

#grab the html off the NYCASP twitter feed
NYCDOT_tweets_dump = requests.get('https://twitter.com/NYCASP')

#Look for text like "suspended", "in effect", and anything
#that looks like a date formatted like {MONTH DAY}
statusRegex = re.compile(r'(suspended|in effect).*\
	((January|February|March|\
	April|May|June|\
	July|August|September|\
	October|November|December) (\d{1,2}))')

#state flags
isSuspendedToday = False
isSuspendedTomorrow = False

#use statusRegex to sift through the tweets dump for the data we need
results = re.findall(statusRegex, NYCDOT_tweets_dump.text)[:2]

#if recent tweets mention "suspended", check when
if any(result[0] == 'suspended' for result in results):	
	for result in results:
		if result[1] == today:						
			isSuspendedToday = True
		elif result[1] == tomorrow:			
			isSuspendedTomorrow = True
		else:
			continue

#do something based on our state flags
if isSuspendedToday and isSuspendedTomorrow:
	print('woo')
elif isSuspendedToday:
	print('suspended today')
elif isSuspendedTomorrow:
	print('suspended tomorrow')
else:
	print('darn')
