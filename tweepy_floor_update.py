import tweepy
from time import ctime


if __name__ == "__main__":

    # From your app settings page
    CONSUMER_KEY = "" # you'll need to generate this
    CONSUMER_SECRET = ""
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    # get access token from the user and redirect to auth URL
    # to get the ACCESS_KEY & ACCESS_SECRET uncomment the code below on the first run 
    
    
    # auth_url = auth.get_authorization_url()
    # print('Authorization URL: ' + auth_url)
    # ask user to verify the PIN generated in broswer
    # verifier = input('PIN: ').strip()
    # auth.get_access_token(verifier)
    # print('ACCESS_KEY = "%s"' % auth.access_token)
    # print('ACCESS_SECRET = "%s"' % auth.access_token_secret)
    # authenticate and retrieve user name

    ACCESS_KEY = ""
    ACCESS_SECRET = ""
    # auth.set_access_token(auth.access_token, auth.access_token_secret)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    f = open("data/curr_floors.txt", "r")
    tweet = "Median Sales Price: " + ctime()+ "\n" + "------------ \n" + f.read() + "------------ \nSee pinned tweet for links to cats"
    api.update_status(tweet)
