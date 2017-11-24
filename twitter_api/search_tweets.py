import twitter_api
api = twitter_api.Api(consumer_key='0Xs6LgdyrYKimVfzYgtk5GhOf', consumer_secret='CG4fLB5gnBf93XRNfvOzoDQcbv1cwOhwCMG4KBw7CXuHhAqlul',
access_token_key='63667277-bkqaeHdLetJO1e9fAyNYic1TaqQWCaDy2GPwyP6vu', access_token_secret='bQxNTV7hNDOvbijwC0uAVq9KmRdmgNBn2fGtyKCAfG0un')

#users = api.GetFriends()
#print([ u for u in users])
params = { 'q' : 'pizza', 'count' : 1 }
tweets = api.search_tweets(params)
print(tweets)
print('\nQUOTA: %s' % api.get_rest_quota())
