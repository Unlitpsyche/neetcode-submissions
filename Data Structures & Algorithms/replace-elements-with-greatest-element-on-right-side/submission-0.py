class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n):
            maximum = -1
            for j in range(i+1,n):
                if arr[j] > maximum:
                    maximum = arr[j]
            arr[i] = maximum
        arr[n-1] = -1
        return arr