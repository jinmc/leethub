class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_int = str(x)
        if str_int[::-1] == str_int:
            return True
        return False