#from typing import List
#import ast
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #hashset = set()
        #n = len(nums)
        #for i in range(n):            
            #if nums[i] in hashset:
                #return True
            #hashset.add(nums[i])
        #return False

        record = []
        for i in range(len(nums)):
            if nums[i] in record:
                return True
            record.append(nums[i])
        return False

#if __name__ == "__main__":   
    #line = input()
    #nums = ast.literal_eval(line.replace("nums=", "").strip())
    #obj = Solution()
    #print(obj.hasDuplicate(nums))