import tweepy
import time

# https://developer.twitter.com/en/docs

auth = tweepy.OAuthHandler("Fake key", "Fake secret")
auth.access_token("Access_token", "Access_token_secret")

api = tweepy.API(auth)

#  read public sweets off of the home timeline
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.txt)

user = api.me()
print(user.name)
print(user.screen_name)
print(user.follower)


def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1)


# Generous bot that always follows back
for follower in tweepy.Cursor(api.followers).items():
    print(follower.name)
    # Then could follow back someone
    # follower.follow()
