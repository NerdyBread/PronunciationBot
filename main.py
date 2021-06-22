import json

import praw

keys = json.loads(open("keys.json").read())

reddit = praw.Reddit(
	client_id = keys["client_id"],
	client_secret = keys["client_secret"],
	password = keys["password"],
	user_agent = keys["user_agent"],
	username= keys["username"]
)

print(reddit.user.me())