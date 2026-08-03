class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            myStringyInt = ""
            for i in digits:
                myStringyInt += str(i) 
            final = str(int(myStringyInt) + 1)
            myStringyArr = []
            for i in final:
                myStringyArr.append(int(i))
            return myStringyArr
        else:
            digits[-1] += 1
        
        return digits