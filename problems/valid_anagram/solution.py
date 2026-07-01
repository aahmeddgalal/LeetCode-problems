class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def count(string):
            letters = {}
            for letter in string:
                if letter in letters:
                    letters[letter] += 1
                else:
                    letters[letter] = 1
            
            return letters
        
        s_letters = count(s)
        t_letters = count(t)

        return s_letters == t_letters



        # if "".join(sorted(s)) == "".join(sorted(t)):
        #     return True
        
        # return False 