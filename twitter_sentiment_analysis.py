import tweepy
import csv
from textblob import TextBlob

consumer_key = 'BDMHBweQzZwimb1mN1C05gYsp'
consumer_secret = '4A3ryMWFIKvC2TYomOUppNNvAyZPrJAApLcLdQhAietfPwEEYE'

access_token = '863173256-8oym2WsCQb8V2XWJZp3CPBNfpiVxLrmfjNAjuBBE'
access_token_secret = 'X3fYTmoRevFv6R6x8OcN7NdNwhpWZ3cEK49doIHIdhVC7'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

public_tweets = api.search('trump')
with open('csvexample.csv', 'w', newline='') as f:
	fieldnames = ['positive polarity', 'negative polarity']
	writer = csv.DictWriter(f, fieldnames = fieldnames)
	writer.writeheader()

	for tweet in public_tweets: 
		print(tweet.text)
		analysis = TextBlob(tweet.text)
		print(analysis.sentiment)

		if analysis.sentiment.polarity > 0.5:		
			# Write a row to the CSV file. I use encode UTF-8
			writer.writerow({'positive polarity': tweet.text.encode('utf-8')})
		else:
			writer.writerow({'negative polarity': tweet.text.encode('utf-8')})
		