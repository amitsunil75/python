numIndexes={}
class Solution:

    def twosum(self,num,target):
       
        for i ,n in enumerate(num):
            complement=target-n
            if complement in  numIndexes:
                return [numIndexes[complement],i]
            numIndexes[n]=i
            print(numIndexes)




solution=Solution()
solution.twosum([9,2,3,5],8)
