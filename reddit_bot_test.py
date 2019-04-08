import praw
import config
import pprint

def bot_login():
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "Reddit Bot Test")
	return r

def run_bot(r):
	for comment in r.subreddit('Animemes').comments(limit=25):
		print(comment.body)
		if "Zero Two" in comment.body:
			print "String found"


print(config.username)

reddit = bot_login()

# assume you have a Reddit instance bound to variable `reddit`
submission = reddit.submission(id='39zje0')
print(submission.title) # to make it non-lazy
pprint.pprint(vars(submission))

#print(reddit.redditor('DIZ001').comments(limit=10))

'''
print(reddit.read_only)

print(reddit.user.me())

subreddit = reddit.subreddit('Animemes')

print(subreddit.display_name)  # Output: redditdev
print(subreddit.title)         # Output: reddit Development
print(subreddit.description)   # Output:  A subreddit description
'''
#run_bot(reddit)