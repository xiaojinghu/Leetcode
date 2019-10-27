class User(object):
    def __init__(self, userID):
        self.ID = userID
        # who the user follows, remember to follow him/herself
        self.followers = set()
        # who follows the user
        self.followees = set([self])
        # what tweets does the user post
        self.tweets = set()
        # the user's news feed
        self.newsFeed = set()
        
class Tweet(object):
    def __init__(self, tweetID, time, userID):
        self.userID = userID
        self.time = time
        self.ID = tweetID
    

class Twitter(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.IDToUser = {}
        self.IDToTweet = {}
        
    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        if userId not in self.IDToUser:
            self.IDToUser[userId] = User(userId)
        user = self.IDToUser[userId]
        self.time += 1
        # generate a new tweet
        newTweet = Tweet(tweetId, self.time, userId)
        # add the tweet to the user's data
        user.tweets.add(newTweet)
        # push the tweet to all of its followees
        for followee in user.followees:
            followee.newsFeed.add(newTweet)
            
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.IDToUser:
            self.IDToUser[userId] = User(userId)
        user = self.IDToUser[userId]
        tweets = list(user.newsFeed)
        tweets.sort(key = lambda x:x.time, reverse = True)
        if len(tweets)<=10:
            return [x.ID for x in tweets]
        return [x.ID for x in tweets[:10]]
        

    def follow(self, followeeId, followerId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.IDToUser:
            follower = User(followerId)
            self.IDToUser[followerId] = follower
        follower = self.IDToUser[followerId]
        if followeeId not in self.IDToUser:
            followee = User(followeeId)
            self.IDToUser[followeeId] = followee
        followee = self.IDToUser[followeeId]
        follower.followees.add(followee)
        followee.followers.add(follower)
        for tweet in follower.tweets:
            followee.newsFeed.add(tweet)

        
    def unfollow(self, followeeId, followerId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.IDToUser:
            self.IDToUser[followerId] = User(followerId)
        if followeeId not in self.IDToUser:
            self.IDToUser[followeeId] = User(followeeId)
        follower = self.IDToUser[followerId]
        followee = self.IDToUser[followeeId]
        if followee not in follower.followees or followee == follower:
            return
        follower.followees.remove(followee)
        followee.followers.remove(follower)
        for tweet in follower.tweets:
            followee.newsFeed.remove(tweet)
