import tweepy
import json

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error detected")

# Authenticate to Twitter

auth = tweepy.OAuthHandler("lX4x5JrUFU3M9oT61ArQveqBp", "h3QOWQAIINxYzRZy618KHlxTOSAb61wAtiLSYXEgXVRJoTwlTf")
auth.set_access_token("2210920084-lNgn4Ptey2XveUJ0SLsGCIzneChjOEnwqaiNWdy", "tmEoHlKVvjIcG9Y55r3Io6guPrxnqxMEdO9XsHd6sBcuc")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

# tweets_listener = MyStreamListener(api)
# stream = tweepy.Stream(api.auth, tweets_listener)
# stream.filter(track=["$TSLA", "$NIO"], languages=["en"])

for tweet in tweepy.Cursor(api.search, q='@JimCramer',result_type='popular').items(5):
    print(tweet)
