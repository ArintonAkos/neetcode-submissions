import heapq

class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.following = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res: List[int] = []

        # User does not follow themselves, but data has to be shown on the feed
        relevant_users = {userId}
        for followee in self.following.get(userId, []):
            relevant_users.add(followee)

        # Create pointer for maximum timestamp post for every followee of the user
        pointers = []
        for relevant_user in relevant_users:
            relevant_user_posts = self.posts.get(relevant_user, [])

            if relevant_user_posts:
                last_index = len(relevant_user_posts) - 1
                timestamp, tweetId = relevant_user_posts[last_index]

                heapq.heappush(pointers, (-timestamp, tweetId, relevant_user, last_index))

        k = 10
        while pointers and k > 0:
            _, tweetId, relevant_user, idx = heapq.heappop(pointers)

            res.append(tweetId)

            if idx > 0:
                last_index = idx - 1
                timestamp, tweetId = self.posts[relevant_user][last_index]

                heapq.heappush(pointers, (-timestamp, tweetId, relevant_user, last_index))

            k -= 1

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            return
        
        self.following[followerId].discard(followeeId)
