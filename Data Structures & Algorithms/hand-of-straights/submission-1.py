class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        if groupSize == 0:
            return False

        if n % groupSize != 0:
            return False

        hand.sort()
        # Freq bucket
        bucket = [0] * 1001

        for num in hand:
            bucket[num] += 1

        # hand = [1,2,4,2,3,5,3,4]
        # indices = [0, 1, 2, 3, 4, 5, .... , 1000
        # bucket  = [0, 1, 2, 2, 2, 1, 0, 0, 0, 0] -> opti: check the max value in the hand, 
        # and create the bucket like [0, max]
        
        # bucket = [0, 1, 2, 2, 2, 1, 0, 0, 0, 0]
        # Becomes
        # bucket = [0, 0, 1, 1, 1, 1, 0, 0, 0, 0]
        # bucket = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # Return true

        #hand = [1,2,3,3,4,5,6,7]
        # bucket = [0, 1, 1, 2, 1, 1, 1, 1]
        # bucket = [0, 0, 0, 1, 0, 1, 1, 1]
        # nums[i] < curr_amount (curr_amount is the starting positions value)
        # Imeddetialy return false
        
        # Also another optimization we cna do: we count how many items have we decresed
        # once N is reached, we can break the for loop

        print(f"Bucket: {bucket[:20]}")
        for i, freq in enumerate(bucket):
            if freq == 0:
                continue
            
            k = 0
            while k < groupSize and i + k < 1002:
                if bucket[i + k] < freq:
                    return False

                bucket[i + k] = bucket[i + k] - freq
                k += 1 

        print(f"Bucket: {bucket[:20]}")
        return True