class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ''' This function sorts the array by parity'''
        even =[] #This list will contain even parity
        odd=[] #This list will contain off parity
        
        for i in A:
            if(i%2==0):
                even.append(i)
            else:
                odd.append(i)
        return (even+odd)
