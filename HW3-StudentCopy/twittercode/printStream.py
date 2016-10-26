import tweepy
import json

# Unique code from Twitter
access_token = "2155414722-RU2WHLoT0IhljfeOzVWeeAak2yIot5S54RvPnLe"
access_token_secret = "	RWftU91xIZBR2ZmbzTbWuZ6OMOcwvtxCTCJI00VCBeazM"
consumer_key = "NL5BZbHPXrkUU5bAUhU2MijrX"
consumer_secret = "iUUZVzhzt8UqXjw5mkuLNZ6nzf0ymlvEFkZBsuNfNAML8H4V0x""

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
def process_or_store(tweet):
	print(tweet.get('user').get('screen_name'))
	print(tweet.get('text').encode('unicode_escape'))
	print(tweet.get('created_at'))

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json) 


for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)


