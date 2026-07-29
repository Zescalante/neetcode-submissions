class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        for val in nums:
            hashmap[val] += 1
        pairs = []

        for val, count in hashmap.items():
            pairs.append([count, val])
        print(pairs)
        pairs.sort(key=lambda x: x[0], reverse=False)
        print(pairs)
        res = []
        for _ in range(k):
            res.append(pairs.pop()[1])
        return res
