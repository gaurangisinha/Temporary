import os
import random
import json
import requests

# Fetch Json
def get_Quote():
    params = {
        'method':'getQuote',
        'lang':'en',
        'format':'json'
    }
    response = requests.get('http://api.forismatic.com/api/1.0/',params)
    jsonText =json.loads(response.text)
    return jsonText["quoteText"],jsonText["quoteAuthor"]


## Number of days you want to make commits
print("""
-------------------------------------------------------------
EVERGREEN BOT -- Welcome to Github commit in the past !! XD
-------------------------------------------------------------

Instructions :
--------------
1. Enter the day number you want to rewind to (start) [Eg..  n = 1 to go to previous day].
2. Enter the number of days you want to perform this action (n).
3. Set the max limit of commit per day(m - Random value taken between 0-m).

Recommended Settings : 
----------------------
1. Set start to any number u want.
2. Set number of days (n = 30).
3. Set max limit ( m = 10 ).

Dangers :
---------
1. If you set n > 180 directly, the script will work but it  may take around 2 days to update your contribution chart.
2. Do not put m > 20 as it will take a long time to finish executing the script.


Samples :
---------
1. With the Recommended settings the script will take 1 min time to execute and the commits will be reflected instantly.


""")

start = int(input("Enter the day number you want to rewind to (Eg : 5 for going 5 days back): "))
if start == 0:
	start = 1
n = int(input("Enter the number of days you want to perform this action (Eg : 10 for going from 5th day, back to 15th day): "))	
maxm = int(input("Enter limit of max commit each day: "))

# Erase contents of the file
file = open("bot.txt","w")
file.close()

for i in range(start,start + n + 1):
	end = random.randint(0,maxm)
	for j in range(0,end):
		d = str(i) + ' day ago'
		try:
		    quote,author = get_Quote()
		    text = str(j) +" " + quote+" -"+author+"\n"
		except:
		    text = "Sorry!! No quote found -- " + str(j) + "\n"

		## Open a text file and modify it (append mode)
		with open('bot.txt', 'a') as file:
		    file.write(text)

		## Add bot.txt to staging area
		os.system('git add bot.txt')

		## Commit it
		os.system('git commit --date="' + d + '" -m "auto commit"')

## push the commit to github
os.system('git push -u origin master')
