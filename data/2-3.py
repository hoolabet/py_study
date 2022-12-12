import tweepy

CONSUMER_KEY = "KJ0R64sdbF76Cz1tgsNdwdyME"
CONSUMER_SECRET = "WD3TwOJx7UrRUMkaHSmnRh66VqS3lRyOosgoLUZsL0TjGIZjVz"
ACCESS_TOKEN_KEY = "1595589114761355264-7OBtiqfVPLgVz9KW1aF279lMNYcsvQ"
ACCESS_TOKEN_SECRET = "ciqLfSronIK76hurTY4FUHMMWMYx9JpiPG7O7OqnVyXPx"

auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)

auth.set_access_token(ACCESS_TOKEN_KEY,ACCESS_TOKEN_SECRET)

api = tweepy.API(auth=auth, wait_on_rate_limit=True)

print(api)
