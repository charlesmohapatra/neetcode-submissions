class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.f_arr = nums
        self.f_arr.sort(reverse = True)
        self.position = k
        

    def add(self, val: int) -> int:
        self.f_arr.append(val)
        self.f_arr.sort(reverse=True)
        return self.f_arr[self.position-1]
        
