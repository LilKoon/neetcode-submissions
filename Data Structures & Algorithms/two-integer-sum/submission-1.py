class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        save = {}

        for i , numi in enumerate(nums):
            numj = target - numi
            if numj in save:
                return [save[numj],i]
            save[numi] = i