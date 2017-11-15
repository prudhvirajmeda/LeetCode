class Solution(object):
    def twoSum(self, nums, target):
        for index_1,i in enumerate(nums):
            for index_2,j in enumerate(nums):
                if i + j == target and index_1 != index_2:
                    return index_1,index_2