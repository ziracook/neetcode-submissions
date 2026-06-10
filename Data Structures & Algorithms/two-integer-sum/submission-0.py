class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSumHashMap(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            n = nums[i]
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[n] = i

        