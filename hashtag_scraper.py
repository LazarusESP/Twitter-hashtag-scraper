import tweepy

# Twitter API
consumer_key = 'your_consumer_key_here'
consumer_secret = 'your_consumer_secret_here'
access_token = 'your_access_token_here'
access_token_secret = 'your_access_token_secret_here'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Scrape popular hashtags
trends = api.trends_place(1)
hashtags = []
for trend in trends[0]["trends"]:
    if trend["name"].startswith('#'):
        hashtags.append(trend["name"])

# export top 10 hashtags to a text file
with open('top_hashtags.txt', 'w') as f:
    f.write("Top 10 trending hashtags on Twitter:\n\n")
    for i in range(10):
        f.write("{0}: {1}\n".format(i+1, hashtags[i]))
print("Top 10 trending hashtags exported to 'top_hashtags.txt'")
