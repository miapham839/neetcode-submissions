# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

'''
- l, r
while l <= r:
    - mid
    - guess(mid)
    - if 0: return mid
    - elif -1: r = mid - 1
    - elif 1: l = mid + 1
'''
class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                r = mid - 1
            elif guess(mid) == 1:
                l = mid + 1

        