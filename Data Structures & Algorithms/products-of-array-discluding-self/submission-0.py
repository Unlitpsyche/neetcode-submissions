class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_o = nums
        nums_i = nums
        ans = []
        for i in range(len(nums_o)):
            product = 1
            for j in range(len(nums_i)):
                if i != j:
                    product *= nums_i[j]
            ans.append(product)
        return ans
