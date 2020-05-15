class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0,0,0] #red, white, blue
        
        # Counting number of each color
        for elem in nums:
            counts[elem] += 1
            
        # Remake array
        a = 0
        for p in range(3):
            r = counts[p]
            for i in range(r):
                nums[a] = p
                a += 1
        
        return nums
                