from tweepy import OAuthHandler, Cursor
from datetime import datetime, timedelta

# Authenticate to Twitter

auth = tweepy.OAuthHandler("lX4x5JrUFU3M9oT61ArQveqBp", "h3QOWQAIINxYzRZy618KHlxTOSAb61wAtiLSYXEgXVRJoTwlTf")
auth.set_access_token("2210920084-lNgn4Ptey2XveUJ0SLsGCIzneChjOEnwqaiNWdy", "tmEoHlKVvjIcG9Y55r3Io6guPrxnqxMEdO9XsHd6sBcuc")

authAPI = API(auth)
collection = []
count = 0
user = authAPI.get_user('@StockTwits')

endDate = datetime.utcnow - timedelta(days=10)

for status in Cursor(authAPI.user_timeline, id = user, tweet_mode = 'extended').items(10):

    if "retweeted_status" in dir(status):
        collection.append(status.retweeted_status.full_text)
    else:
        collection.append(status.full_text)

    if status.created_at < endDate:
        break

print(collection)

"""
with open('tweets.txt', 'w') as fileWrite:
    for item in collection:
        text = item.split("\n")
        text = ' '.join(text).split()
        fileWrite.write(' '.join(text))
        fileWrite.write('\n')
"""