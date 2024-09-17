#!/usr/bin/env python3

class Twitter:

    def __init__(self):
        from collections import defaultdict
        self.following = defaultdict(set)
        self.posts = defaultdict(list)
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.t, tweetId))
        self.t -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []

        self.following[userId].add(userId)
        for user in self.following[userId]:
            if user in self.posts:
                t, tweet = self.posts[user][-1]
                next_idx = len(self.posts[user]) - 2
                min_heap.append((t, next_idx, user, tweet))
        heapq.heapify(min_heap)
        newsFeed = []
        while min_heap and len(newsFeed) < 10:
            _, next_idx, user, tweet = heapq.heappop(min_heap)
            newsFeed.append(tweet)
            if next_idx >= 0:
                t, tweet_to_add = self.posts[user][next_idx]
                heapq.heappush(min_heap, (t, next_idx-1, user, tweet_to_add))
            
        return newsFeed


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

