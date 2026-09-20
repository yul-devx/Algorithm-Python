# 해시테이블, 문자열, 정렬
## 0242. Valid Anagram

### 접근방법: 해시테이블
### 시간복잡도: O(n)
### 공간복잡도: O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        anagram_set = set(s)
        anagram_dict = {}

        for sdx in s:
            anagram_dict[sdx] = anagram_dict.get(sdx, 0) + 1

        for tdx in t:
            if tdx not in anagram_set:
                return False

            anagram_dict[tdx] -= 1

            if anagram_dict[tdx] < 0:
                return False   
        
        return True   

if __name__ == "__main__":

    sol = Solution()

    answer1 = sol.isAnagram("anagram", "nagaram")
    answer2 = sol.isAnagram("rat", "car")
    answer3 = sol.isAnagram("rat", "cardd")

    print(answer1)  # true
    print(answer2)  # false
    print(answer3)  # false
