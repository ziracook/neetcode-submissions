class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while start < end:
            if (numbers[start] + numbers[end]) == target:
                return [start + 1, end + 1]
            elif (end - start) == 1: # If 1 away from eachother, reset
                start += 1
                end = len(numbers) - 1
            else:
                end -= 1



        