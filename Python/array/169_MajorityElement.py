from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums:List[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate
        

def main():
    nums = [2,2,1,1,1,2,2]
    MajEle = Solution()
    print(MajEle.majorityElement(nums))

if __name__ == '__main__':
    main()
