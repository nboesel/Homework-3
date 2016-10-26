import tweepy
from textblob import TextBlob

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

public_tweets = api.search('"Gilmore Girls" @netflix')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)


#polarity -- measures how positive or negative
#subjectivity -- measures how factual.

#1 Sentiment Analysis - Understand and Extracting Feelings from Data
