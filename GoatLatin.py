class Solution:
    def isVowel(self,d):
        #vowels in english
        if(d == 'a' or d =='e' or d =='i' or d =='o' or d =='u'):
            return True
        else:
            return False
        
    def toGoatLatin(self, S: str) -> str:
        S = S.split(' ')
        l = len(S)
        for i in range(0,l):
            toAppend = 'a'*(i+1)
            if not self.isVowel((S[i][0]).lower()):
                S[i] = S[i][1:]+S[i][0]
            S[i] = S[i]+'ma'+toAppend
        
        ans = ''
        for i in range(0,l):
            if(i+1>=l):
                ans = ans+S[i]
            else:
                ans = ans+S[i]+' '
        
        return ans
        
