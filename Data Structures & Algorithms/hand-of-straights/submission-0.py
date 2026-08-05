class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hashmap = Counter(hand)

        # hashmap = defaultdict(int)
        # for val in hand:
        #     hashmap[val] += 1

        hand.sort()
        for val in hand:
            if hashmap[val] == 0:
                continue
                
            for i in range(val, val + groupSize):
                if i in hashmap and hashmap[i] > 0:
                    hashmap[i] -= 1
                else: 
                    return False

        return True
# time: O(nlogn)
# space: O(n)