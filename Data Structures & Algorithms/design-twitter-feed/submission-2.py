import heapq

class Twitter:

    def __init__(self):
        self.posts = []
        self.following = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.posts, (-self.timestamp, tweetId, userId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # print(f"userid: {userId} | posts: {self.posts} | following: {self.following}")
        res: List[int] = []

        # User does not follow themselves, but data has to be shown on the feed
        relevant_users = set([userId])

        for followee in self.following.get(userId, []):
            relevant_users.add(followee)

        posts_copy = self.posts.copy()

        k = 10
        while k > 0 and posts_copy:
            _, tweet_id, user_id = heapq.heappop(posts_copy)

            if user_id in relevant_users:
                k -= 1
                res.append(tweet_id)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            return
        
        self.following[followerId].discard(followeeId)
