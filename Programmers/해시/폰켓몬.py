# 해시
## 폰켓몬

def solution(nums):
    return min(len(set(nums)), len(nums)//2)   

if __name__ == "__main__":
    answer1 = solution([3,1,2,3])
    answer2 = solution([3,3,3,2,2,4])
    answer3 = solution([3,3,3,2,2,2])

    print(answer1)    # 2
    print(answer2)    # 3
    print(answer3)    # 2