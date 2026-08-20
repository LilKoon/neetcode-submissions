class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        save = list()

        for i , numi in enumerate(nums):
            numj = target - numi
            if numj in save:
                return [save.index(numj),i]
            save.append(numi)