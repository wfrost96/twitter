import twitter

twitter_handle = "@user"
date_since = "2020-03-01"

twitter_consumer_key = ''
twitter_consumer_secret = ''
twitter_access_token = ''
twitter_access_secret = ''

twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret, tweet_mode='extended')

list_of_tweets = []

statuses = twitter_api.GetUserTimeline(screen_name=twitter_handle, count=1, include_rts=1)
earliest_tweet_id = 0
for status in statuses:
    earliest_tweet_id = status.id
    print(earliest_tweet_id)
    print(status.created_at)
    list_of_tweets.append(status.id)
print("Earliest Tweet id:", earliest_tweet_id)

for i in range(1, 3):
    print(earliest_tweet_id)
    earliest_tweet_id = earliest_tweet_id - 1
    statuses = twitter_api.GetUserTimeline(screen_name=twitter_handle, max_id=earliest_tweet_id, count=2, include_rts=1)
    for status in statuses:
        earliest_tweet_id = status.id
        print(earliest_tweet_id)
        print(status.created_at)
        list_of_tweets.append(status.id)
    print("Earliest Tweet id:", earliest_tweet_id)

print(list_of_tweets)
