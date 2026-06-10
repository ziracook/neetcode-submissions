class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsmap = {}
        freq = [[] for i in range(len(nums) + 1)]

        # Creates map of number and frequency
        for n in nums:
            numsmap[n] = 1 + numsmap.get(n, 0)

        
        # For each number and count, add number to frequency list
        for n, c in numsmap.items():
            freq[c].append(n)
        
        res = []
        # Traverse in reverse order
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)

                if len(res) >= k:
                    return res