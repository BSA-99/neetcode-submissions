class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp+=1
        self.tweets[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.follows[userId] | {userId}
        heap = []

        for user in users:
            if self.tweets[user]:
                index = len(self.tweets[user])-1
                timestamp, tweetId = self.tweets[user][index]
                heapq.heappush(heap, (-timestamp, tweetId, user, index))
        feed = []
        while heap and len(feed)<10:
            timestamp, tweetId, user, index = heapq.heappop(heap)
            feed.append(tweetId)
            if index>0:
                next_index = index-1
                timestamp, tweetId = self.tweets[user][next_index]
                heapq.heappush(heap, (-timestamp, tweetId, user, next_index))
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)

        
