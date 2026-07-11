class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = sorted(nums)
        group = []

        for i in range(len(arr)):
            j = i + 1
            k = len(arr) - 1

            while j < k:
                total = arr[i] + arr[j] + arr[k]

                if total == 0:
                    triplet = [arr[i], arr[j], arr[k]]

                    if triplet not in group:
                        group.append(triplet)

                    j += 1
                    k -= 1

                elif total < 0:
                    j += 1

                else:
                    k -= 1

        return group