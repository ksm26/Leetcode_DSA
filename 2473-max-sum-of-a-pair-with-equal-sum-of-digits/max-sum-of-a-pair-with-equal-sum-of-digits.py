class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def get_digit_sum(num):
            digitsum = 0 
            while num:
                digitsum += num%10
                num = num //10
            return digitsum

        numdict = {}
        count = -1 

        for num in nums :
            digitsum = get_digit_sum(num)
            if digitsum in numdict:
                count = max(count,num + numdict[digitsum])

                numdict[digitsum] = max(num, numdict[digitsum])
            else : 
                numdict[digitsum] = num

        return count

        