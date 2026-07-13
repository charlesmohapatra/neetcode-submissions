class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        def merged(arr, s, m, e):
            L = arr[s:m+1]
            R = arr[m+1:e+1]
            i = 0
            j = 0
            k = s
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        def mergeSort(arr, s, e):
            if e-s+1 <= 1:
                return arr
            m = (e+s)//2
            mergeSort(arr, s, m)
            mergeSort(arr, m+1, e)
            merged(arr, s, m, e)
        mergeSort(nums1 , 0, m+n-1)