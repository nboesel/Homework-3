import tweepy
import nltk

# Unique code from Twitter
access_token = "2155414722-RU2WHLoT0IhljfeOzVWeeAak2yIot5S54RvPnLe"
access_token_secret = "	RWftU91xIZBR2ZmbzTbWuZ6OMOcwvtxCTCJI00VCBeazM"
consumer_key = "NL5BZbHPXrkUU5bAUhU2MijrX"
consumer_secret = "iUUZVzhzt8UqXjw5mkuLNZ6nzf0ymlvEFkZBsuNfNAML8H4V0x"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search('UMSI')


adj_count = 0;

for tweet in public_tweets:
	print(tweet.text)
	tagged_tokens = nltk.pos_tag(tweet.text) # gives us a tagged list of tuples
	for (word, tag) in tagged_tokens:
		if tag == "JJ":
			adj_count+=1

print("There were ", adj_count,"adjectives in your tweets")
	
#Learn more about Search
#https://dev.twitter.com/rest/public/search

