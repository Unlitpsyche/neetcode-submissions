class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        record = []
        for i in range(len(nums)-k+1):
            record.append(max(nums[i:i+k]))
        return record


                