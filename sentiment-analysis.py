import tweepy
from textblob import TextBlob
import csv
import sys
import re

# Step 1 - Authenticate
consumer_key= 'CONSUMER_KEY_HERE'
consumer_secret= 'CONSUMER_SECRET_HERE'

access_token='ACCESS_TOKEN_HERE'
access_token_secret='ACCESS_TOKEN_SECRET_HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search(sys.argv[1])

def clean_tweet(tweet):
    tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet).split())
    #print ('AFTER regex: \n ',tweet,'\n')
    return tweet

f = open(sys.argv[2], 'wt')
try:
    writer = csv.writer(f)
    writer.writerow(('Tweet', 'Sentiment'))

    for tweet in public_tweets:
        
        cleaned_tweet = clean_tweet(tweet.text) 
        analysis = TextBlob(cleaned_tweet)
        

        if(analysis.sentiment.polarity>0):
            sentiment = 'POSITIVE'
        elif (analysis.sentiment.polarity==0):
            sentiment = 'NEUTRAL'
        else :
            sentiment = 'NEGATIVE'
        
        writer.writerow((cleaned_tweet,sentiment))

finally:
    f.close()

print (open(sys.argv[2], 'rt').read())