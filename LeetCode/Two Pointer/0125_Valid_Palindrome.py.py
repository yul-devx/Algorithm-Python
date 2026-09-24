# Two Pointers, String
## 125. Valid Palindrome

### 접근방법: 문자열, 투포인터
### 시간복잡도: O(n)
### 공간복잡도: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:

        sdx = 0
        edx = len(s) - 1

        while sdx < edx: 

            while sdx < edx and not s[sdx].lower().isalnum():
                sdx += 1

            while sdx < edx and not s[edx].lower().isalnum():
                edx -= 1

            if s[sdx].lower() != s[edx].lower():
                return False

            sdx += 1
            edx -= 1

        return True

if __name__ == "__main__":

    sol = Solution()

    answer1 = sol.isPalindrome("A man, a plan, a canal: Panama")
    answer2 = sol.isPalindrome("race a car")
    answer3 = sol.isPalindrome(" ")
    answer4 = sol.isPalindrome(".,")

    print(answer1)  # True
    print(answer2)  # False
    print(answer3)  # True
    print(answer4) # 
