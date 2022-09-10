"""
the ransom note problem of the leet code
if the string can be construted using the other string 
"""

#test case 
ransomNote = "a"
magazine = "b"
Output = false

ransomNote2 = "aa"
magazine2 = "ab"
Output2 = false

ransomNote3 = "aa"
magazine3 = "aab"
Output3 = true


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        The function to find the similar string in the two strings
        Args: 
        	ransomNOte (str) : the first string 
        	magazine (str) : the secomd string 
 		Returns:
 			true or false (bool) : the value if corret or not 
        """

        for i in ransomNote:
        	if i not in magazine:
        		return False

        	return True
        
