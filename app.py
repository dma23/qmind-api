from tweepy import OAuthHandler,API, Cursor
from datetime import datetime, timedelta

# Authenticate to Twitter

auth = OAuthHandler("WBgiGIh9S0a35o3l85w5y9hl8", "xmtLzSSO8nJgh6TStbRD0k0N91TpWfNZ6iREQDjIciGFqrj6G8")
auth.set_access_token("2210920084-ukDZsTm1GWU3kNQip9Bk5o5EWGOAZpYP5rDa2pU", "zsH2103FjgAI0nQIW5uUaxA2kqzsRc5xQlFAHSDfdIrpZ")

'''userName = [
    '@CNBC',
    '@WSJmarkets'
    #,'@StockTwits'
    ]
'''
userName = '@Bespokeinvest' 
allTweets = []


authAPI = API(auth)
user = authAPI.get_user(userName)

# We create a loop continously to collect data as much as we need i.e., here we are collecting till the endDate.

#for accounts in userName:
for status in Cursor(authAPI.user_timeline, id = userName, tweet_mode = 'extended', include_rts=False, exclude_replies=True).items(50):
        
    data = (
        status.user.name,
        status.created_at,
        status.full_text,
    )

    allTweets.append(data)

with open('tweets.txt', 'w') as fileWrite:
    for item in allTweets:
        fileWrite.write(str(item))
        fileWrite.write('\n')