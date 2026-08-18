class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        listRong = list()
        for i in range(len(nums)):
            if nums[i] in listRong:
                return True
            else:
                listRong.append(nums[i])
        return False
