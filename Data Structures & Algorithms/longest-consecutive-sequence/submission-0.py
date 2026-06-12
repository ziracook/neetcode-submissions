class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for n in nums:
            # Check if start of a sequence
            if (n - 1) not in numset:
                currLen = 0 # New sequence length

                # While it has the next consecutive number
                while (n + currLen) in numset:
                    currLen += 1
                longest = max(currLen, longest)
        return longest