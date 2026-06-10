import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsmap = {}

        # Creates map of number and frequency
        for n in nums:
            numsmap[n] = 1 + numsmap.get(n, 0)

        # Get the k most frequent numbers
        heap = []
        for t in numsmap:
            heapq.heappush(heap, (-1 * numsmap[t], t))
        
        res = []
        for i in range(k):
            curmax = heapq.heappop(heap)
            res.append(curmax[1])

        return res

        