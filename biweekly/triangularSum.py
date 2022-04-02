class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
        
        while len(nums) > 1: 
            newNums = [(nums[i] + nums[i+1]) % 10 for i in range(0, len(nums) - 1)]
            nums = newNums
     
        return nums[0]