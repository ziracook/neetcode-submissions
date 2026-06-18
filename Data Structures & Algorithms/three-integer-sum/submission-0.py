class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            curval = nums[i]

            if curval > 0:
                break

            # Skip duplicates
            if i > 0 and curval == nums[i - 1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            
            while j < k:
                cursum = curval + nums[j] + nums[k]
                if cursum > 0:
                    k -= 1
                elif cursum < 0:
                    j += 1
                else:
                    res.append([curval, nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # Skip duplicates
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1


        return res