from twitterpandas import TwitterPandas
from examples.keys import TWITTER_OAUTH_SECRET, TWITTER_OAUTH_TOKEN, TWITTER_CONSUMER_SECRET, TWITTER_CONSUMER_KEY

__author__ = 'willmcginnis'


def friendship_option():
    # get our own user id
    user_id = tp.api_id

    # use it to find all of our own friends (people we follow)
    df = tp.friends_friendships(id_=user_id, rich=True)
    total_friends = df.shape[0]

    # filter the df down to only those who don't follow us back
    df = df[df['target_follows_source'] == False]

    # print out the info:
    print('A total of %d of those who I follow on twitter, don\'t follow me back.' % (df.shape[0], ))
    print('...that\'s about %4.2f%% of them.\n' % ((float(df.shape[0]) / total_friends) * 100, ))
    print(df['target_user_screen_name'].values.tolist())


def user_method_option():
    # get our own user id
    user_id = tp.api_id

    # use it to find all of our own friends (people we follow)
    # TODO: friends in user module, equivalent of followers.
    df = tp.friends(id_=user_id)
    total_friends = df.shape[0]

    # filter the df down to only those who don't follow us back
    df = df['followed_by' == False]

    # print out the info:
    print('A total of %d of those who I follow on twitter, don\'t follow me back.' % (df.shape[0], ))
    print('...that\'s about %4.2f%% of them.\n' % ((float(df.shape[0]) / total_friends) * 100, ))
    print(df['screen_name'].values.tolist())

if __name__ == '__main__':
    # create a twitter pandas client object
    tp = TwitterPandas(
        TWITTER_OAUTH_TOKEN,
        TWITTER_OAUTH_SECRET,
        TWITTER_CONSUMER_KEY,
        TWITTER_CONSUMER_SECRET
    )

    friendship_option()
    # user_method_option()
