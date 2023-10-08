class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_so_far = -1
        for i in range(n-1, -1, -1):
            curr = arr[i]
            arr[i] = max_so_far
            if curr > max_so_far:
                max_so_far = curr
        return arr