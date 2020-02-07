import twitter

def run():
    # Set up API
    print('Setting up Twitter API')
    consumer_key='CONSUMER_API_KEY'
    consumer_secret='CONSUMER_API_SECRET_KEY'
    access_token_key='ACCESS_TOKEN'
    access_token_secret='ACCESS_TOKEN_SECRET'
    api = twitter.Api(consumer_key, consumer_secret, access_token_key, access_token_secret)

    # Verify the api credentials
    print(api.VerifyCredentials())

    # Sending tweet
    print('Sending tweet')
    tweet = 'Insert message here 2' # This is the tweet message
    res = api.PostUpdate(tweet)
    print('Finished sending tweet\n result: {}'.format(res))

if __name__ == '__main__':
    run()
