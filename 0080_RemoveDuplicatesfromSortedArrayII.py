class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr, newLength = -1, 0
        flag = False
        
        i = 0
        while newLength != len(nums):
            if nums[i] == curr:
                if flag == False:
                    flag = True
                    newLength += 1
                    i += 1
                else:
                    nums.pop(i)
            else:
                curr = nums[i]
                flag = False
                newLength += 1
                i+=1
        
        return newLength