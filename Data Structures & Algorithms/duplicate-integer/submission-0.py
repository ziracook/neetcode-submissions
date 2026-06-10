class Solution:
    def hasDuplicate1(self, nums: List[int]) -> bool:
        numsSet = set(nums)
        return len(nums) != len(numsSet)

    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)

        return False