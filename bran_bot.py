import praw
import config
import pprint
import time

def bot_login():
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "Reddit Bot Test")
	return r

def isTopLevelComment(comment):
	result = False
	if comment.parent_id == comment.link_id:
		result = True

	return result

#Function came from Github user acini praw-antiabuse-functions/anti-abuse.py
def haveIReplied(comment):
	ihavenot = True
	numofr = 0
	try:
		repliesarray = comment.replies
		numofr = len(list(repliesarray))
	except:
		pass
	if numofr != 0:
		for repl in comment.replies:
			if repl.author != None and repl.author.name == config.username:
				ihavenot = False
				continue
	if ihavenot:
		return True
	else:
		return False


def branBot(r, comList, subRed):
	print("Entering r/" + subRed)
	for sub in r.subreddit(subRed).hot(limit=1):
		print("Title:  " + sub.title)
		sub.comments.replace_more(limit=None)
		for com in sub.comments:
			if haveIReplied(com):
				if isTopLevelComment(com):
					if "Bran" and "stare" in com.body:
						if com.id not in comList:
							comList.append(com.id)
							global numberOfPost 
							numberOfPost += 1
							com.reply("[***Stare Intensifies***](https://imgur.com/RS7qwc0)")
							print("Post #" + str(numberOfPost) + "\tComId: " + com.id)
							print("Sleeping for 15 mins")
							time.sleep(900)
	
	#print("Number of post made in subreddit: " + str(numberOfPost))
	print("Leaving r/" + subRed)


numberOfPost = 0
commentsRepliedTo = []
subRedArr = ['freefolk', 'gameofthrones']

reddit = bot_login()

while True:
	for sub in subRedArr:
		branBot(reddit, commentsRepliedTo, sub)