import tweepy
import json
import random

def lambda_handler(event, context):

    with open('gentext_total_four.json', 'r') as out:
        tweets = json.load(out)

    random_tweet = random.choice(tweets)

    consumer_key = 'your key here'
    consumer_secret = 'your key here'
    access_token = 'your key here' 
    access_token_secret = 'your key here'

    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)

    api = tweepy.API(auth)

    tweet_post_result = api.update_status(random_tweet)
    
    return {
        'statusCode': 200,
        'body': json.dumps('It worked!')
    }