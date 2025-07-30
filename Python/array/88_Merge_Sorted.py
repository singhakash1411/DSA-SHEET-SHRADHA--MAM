from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        insert = m + n - 1
        while m > 0 and n > 0:
            if nums2[n - 1] > nums1[m - 1]:
                nums1[insert] = nums2[n - 1]
                n -= 1
            else:
                nums1[insert] = nums1[m - 1]
                m -= 1 
            insert -= 1

        if n > 0:
            nums1[:n] = nums2[:n]

def main():
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    MerSorArr = Solution()
    MerSorArr.merge(nums1, m, nums2, n)
    print(nums1)

if __name__ == '__main__':  
    main()

